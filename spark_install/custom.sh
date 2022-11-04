#!/bin/bash
# Simple script for deploying Spark in standalone mode on DAS-5 for the DDPS course 2022.
# Modification of the script by Original Author: Yuxuan Zhao

set -eu

if [[ $# -lt 1 ]] ; then
	echo ""
	echo "usage: source deploy_spark.sh [nodes]"
	echo "for example: source deploy_spark.sh node105,node106,node107"
	echo ""
	exit 1
fi

echo "Deploying spark on ${1}"
nodes=${1}
IFS=',' read -ra node_list <<< "$nodes"; unset IFS
master=${node_list[0]}
worker=${node_list[@]:1}
echo "master is "$master
echo "worker is "$worker

#Comment out these lines if you already downloaded them.
wget -O /var/scratch/$USER/spark-2.4.0-bin-hadoop2.7.tgz https://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz && \
tar -xf /var/scratch/$USER/spark-2.4.0-bin-hadoop2.7.tgz -C /var/scratch/$USER && mv /var/scratch/$USER/spark-2.4.0-bin-hadoop2.7 /var/scratch/$USER/spark

source export.sh

cd /var/scratch/$USER/spark/conf && cp spark-env.sh.template spark-env.sh

sleep 3
echo "export JAVA_HOME=/var/scratch/$USER/jre1.8.0_351" >> spark-env.sh
echo "export SPARK_MASTER_HOST=$master" >> spark-env.sh
echo "export PYSPARK_PATH=/bin/python" >> spark-env.sh
echo "export PYSPARK_PYTHON=/bin/python" >> spark-env.sh
echo "export SPARK_HOME=/var/scratch/ddps2212/spark"
echo "$worker" > workers

ssh $master "cd /var/scratch/$USER/spark"
