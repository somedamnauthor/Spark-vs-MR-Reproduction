Reproducibility Study of 'Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing'

Link to Paper: https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf

To run Spark Experiment 1:

preserve -# 3 -t 02:00:00
source export.sh
source custom.sh <nodes> 
/var/scratch/$USER/spark/bin/spark-submit intQ.py 

Data at: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data
