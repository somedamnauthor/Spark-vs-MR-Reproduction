#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""
Modified from the pre-provided example script : $SPARK_HOME/examples/src/main/python/pagerank.py

Experiment that runs 10 iterations of PageRank on a twitter dataset. On the 6th iteration it decouples one of the worker nodes by cancelling the reservation
Note that the reservation ID has to be hardcoded

Example Usage: (Note that 2 arguments are given apart from the script name - the local path to the file and the number of iterations)
$SPARK_HOME/bin/spark-submit --master spark://10.141.0.16:7077 pagerank.py twitter_combined.txt 10
"""

import re
import sys
import time
import os
from operator import add

from pyspark.sql import SparkSession

def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)

def parseNeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]

if __name__ == "__main__":

    print("Python version:", sys.version)

    # Initialize the spark context.
    spark = SparkSession\
        .builder\
        .appName("PythonPageRank")\
        .getOrCreate()

    # Loads in input file. It should be in format of:
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     ...
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    # Loads all URLs from input file and initialize their neighbors.
    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()

    # Loads all URLs with other URL(s) link to from input file and initialize ranks of them to one.
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    iterTimes = []

    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in range(int(sys.argv[2])):

        # On the 6th iteration, cancel the hardcoded reservation ID
        if iteration==5:
            os.system("module add prun")
            os.system("preserve -c 317368")
        
        # Start time calculation here
        start = time.time()

        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

        # An action here is carried out to trigger the transformations above and help measure the time of iteration
        for (link, rank) in ranks.collect():
        	#print("%s has rank: %s." % (link, rank))
            print('')

        # End time calculation here
        end = time.time()

        # Store the times of each iteration in a list
        iterTimes.append(end-start)


    # Collects all URL ranks and dump them to console.
    for (link, rank) in ranks.collect():
        print("%s has rank: %s." % (link, rank))

    # Write iteration times out onto a file
    with open('out_pagerankTimes.txt', 'w') as f:
    	for line in iterTimes:
        	print >> f, line

    spark.stop()

