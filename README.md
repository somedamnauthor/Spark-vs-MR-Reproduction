## Reproducibility Study of 'Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing'

#### Link to Paper 

https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf

#### Steps for Experiments

```
preserve -# 3 -t 02:00:00
source export.sh
source custom.sh <nodes>
```

Experiment 1:
```
$SPARK_HOME/bin/spark-submit --master <master_node_IP>:<port> pagerank.py <data_file> 10
```

Experiment 2:
```
$SPARK_HOME/bin/spark-submit --master <master_node_IP>:<port> intQ.py 
```

#### Data 

Experiment 1: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data

Experiment 2: https://snap.stanford.edu/data/twitter_combined.txt.gz


