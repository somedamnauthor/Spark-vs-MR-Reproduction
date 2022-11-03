"""
Experiment for interactive queries on Spark
This file focuses on all the queries run in the previous experiment and runs them all sequentially 
The experiment is run on 3 variants of the dataset at sizes 1.8, 3.6 and 5.4GB respectively. 
Average run times are written out onto a .txt file with the same name as this script 

Example Usage:
  $SPARK_HOME/bin/spark-submit --master spark://10.141.0.16:7077 intQ.py
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
        print("NUMBER OF CRIMES ON STREETS:",data.filter(data['Location Description']=="STREET").count(),"\n\n")
        end = time.time()
        time1.append(end-start)
    time1avg = sum(time1) / float(len(time1))

    # Experiment on medium dataset
    for i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES ON STREETS:",dataTwo.filter(dataTwo['Location Description']=="STREET").count(),"\n\n")
        end = time.time()
        time2.append(end-start)
    time2avg = sum(time2) / float(len(time2))

    # Experiment on large dataset
    for i in range(3):
        start = time.time()
        print("NUMBER OF CRIMES ON STREETS:",dataThree.filter(dataThree['Location Description']=="STREET").count(),"\n\n")
        end = time.time()
        time3.append(end-start)
    time3avg = sum(time3) / float(len(time3)) 

    # Write out the averaged times for all three datasets 
    ex1 = [time1avg,time2avg,time3avg]
    with open('out_matchCount.txt', 'w') as f:
    	for line in ex1:
        	print >> f, line
            
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


    time1 = []
    time2 = []
    time3 = []

    # Experiment on small dataset
    for i in range(3):
        start = time.time()
        data.agg({'Latitude':'avg','Longitude':'avg'}).show()
        end = time.time()
        time1.append(end-start)
    time1avg = sum(time1) / float(len(time1))

    # Experiment on medium dataset
    for	i in range(3):
        start = time.time()
        dataTwo.agg({'Latitude':'avg','Longitude':'avg'}).show()
        end = time.time()
        time2.append(end-start)
    time2avg = sum(time2) / float(len(time2))

    # Experiment on large dataset
    for i in range(3):
        start = time.time()
        dataThree.agg({'Latitude':'avg','Longitude':'avg'}).show()
        end = time.time()
        time3.append(end-start)
    time3avg = sum(time3) / float(len(time3))

    # Write out the averaged times for all three datasets 
    ex3 = [time1avg,time2avg,time3avg]
    with open('out_avgs.txt', 'w') as f:
        for line in ex3:
                print >> f, line

    spark.stop()