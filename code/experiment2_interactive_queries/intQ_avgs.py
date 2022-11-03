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
An example demonstrating Logistic Regression Summary.
Run with:
  bin/spark-submit examples/src/main/python/ml/logistic_regression_summary_example.py
"""
# $example on$
from pyspark.ml.classification import LogisticRegression
# $example off$
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("LogisticRegressionSummary") \
        .getOrCreate()

    # Load training data
    data = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    data2 = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    data3 = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    dataTwo = data.union(data2)
    dataThree = dataTwo.union(data3)

    print("\n\n-------------------------------------------------------------------------------")
    #print("DATA TYPE:",type(dataFull))
    #dataFull.show(5)
    #print("NUMBER OF ROWS:",data.count(),"\n\n")

    """ 
    time1 = []
    time2 = []
    time3 = []

    for i in range(3):
    	start = time.time()
    	print("NUMBER OF CRIMES ON STREETS:",data.filter(data['Location Description']=="STREET").count(),"\n\n")
    	end = time.time()
    	time1.append(end-start)
    	#print("OP TOOK:",time1)
    time1avg = sum(time1) / float(len(time1))

    for i in range(3):
    	start = time.time()
    	print("NUMBER OF CRIMES ON STREETS:",dataTwo.filter(dataTwo['Location Description']=="STREET").count(),"\n\n")
    	end = time.time()
    	time2.append(end-start)
    	#print("OP TOOK:",time2)
    time2avg = sum(time2) / float(len(time2))

    for i in range(3):
    	start = time.time()
    	print("NUMBER OF CRIMES ON STREETS:",dataThree.filter(dataThree['Location Description']=="STREET").count(),"\n\n")
    	end = time.time()
    	time3.append(end-start)
    	#print("OP TOOK:",time3)
    time3avg = sum(time3) / float(len(time3)) 

    ex1 = [time1avg,time2avg,time3avg]

    with open('out_matchCount.txt', 'w') as f:
    	for line in ex1:
        	print >> f, line


    time1 = []
    time2 = []
    time3 = []
    
    for i in range(3):
    	start = time.time()
    	print("NUMBER OF CRIMES IN AM:",data.filter(col("Date").contains("PM")).count())    
    	end = time.time()
    	#print("OP SUB TOOK:",end-start)
        time1.append(end-start)
    time1avg = sum(time1) / float(len(time1))

    for	i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES IN AM:",dataTwo.filter(col("Date").contains("PM")).count())
        end = time.time()
        #print("OP SUB TOOK:",end-start)
       	time2.append(end-start)
    time2avg = sum(time2) / float(len(time2))

    for	i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES IN AM:",dataThree.filter(col("Date").contains("PM")).count())
        end = time.time()
        #print("OP SUB TOOK:",end-start)
       	time3.append(end-start)
    time3avg = sum(time3) / float(len(time3))

    ex2 = [time1avg,time2avg,time3avg]

    with open('out_subMatchCount.txt', 'w') as f:
        for line in ex2:
                print >> f, line
   
    """

    time1 = []
    time2 = []
    time3 = []

    for i in range(3):
    	start = time.time()
    	data.agg({'Latitude':'avg','Longitude':'avg'}).show()
    	end = time.time()
    	#print("AVG TOOK:",end-start)
        time1.append(end-start)
    time1avg = sum(time1) / float(len(time1))

    for	i in range(3):
        start = time.time()
        dataTwo.agg({'Latitude':'avg','Longitude':'avg'}).show()
        end = time.time()
        #print("AVG TOOK:",end-start)
       	time2.append(end-start)
    time2avg = sum(time2) / float(len(time2))

    for i in range(3):
        start = time.time()
        dataThree.agg({'Latitude':'avg','Longitude':'avg'}).show()
        end = time.time()
        #print("AVG TOOK:",end-start)
        time3.append(end-start)
    time3avg = sum(time3) / float(len(time3))

    ex3 = [time1avg,time2avg,time3avg]

    with open('out_avgs.txt', 'w') as f:
        for line in ex3:
                print >> f, line


    spark.stop()

