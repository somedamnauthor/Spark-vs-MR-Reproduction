"""
Experiment for interactive queries on Spark
This file focuses on a query that runs a sub-string match on one column and retrieves the count of those rows
The experiment is run on 3 variants of the dataset at sizes 1.8, 3.6 and 5.4GB respectively. 
Average run times are written out onto a .txt file with the same name as this script 

Example Usage:
  $SPARK_HOME/bin/spark-submit --master spark://10.141.0.16:7077 intQ_subMatchCount.py
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName("LogisticRegressionSummary") \
        .getOrCreate()

    # Load data - ideally we should have different data in all three datasets, but for the purpose of the experiment it doesn't matter
    data = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    data2 = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    data3 = spark.read.csv("/var/scratch/ddps2212/data/crimesData/crimes_full.csv", inferSchema="true", header="true")
    dataTwo = data.union(data2)
    dataThree = dataTwo.union(data3)
    # data, dataTwo and dataThree are the three final datasets

    # initializing arrays that hold the run-times for all three repetitions
    # Each array holds the times for three reps
    time1 = []
    time2 = []
    time3 = []
    
    # Experiment on small dataset
    for i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES IN AM:",data.filter(col("Date").contains("PM")).count())    
        end = time.time()
        time1.append(end-start)
    time1avg = sum(time1) / float(len(time1))

    # Experiment on medium dataset
    for	i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES IN AM:",dataTwo.filter(col("Date").contains("PM")).count())
        end = time.time()
        time2.append(end-start)
    time2avg = sum(time2) / float(len(time2))

    # Experiment on large dataset
    for	i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES IN AM:",dataThree.filter(col("Date").contains("PM")).count())
        end = time.time()
        time3.append(end-start)
    time3avg = sum(time3) / float(len(time3))

    # Write out the averaged times for all three datasets 
    ex2 = [time1avg,time2avg,time3avg]
    with open('out_subMatchCount.txt', 'w') as f:
        for line in ex2:
                print >> f, line

    spark.stop()