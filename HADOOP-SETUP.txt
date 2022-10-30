Steps:

mkdir and cd into /local/ddps2212 on the master node


Wget the hadoop bin file on the master node - https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz


Untar the tar with tar xvzf on master node

Edit etc/hadoop/core-site.xml on all nodes: 
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://server-ip:9000</value>
    </property>
</configuration>

Edit etc/hadoop/hdfs-site.xml on all nodes:
<configuration>
   <property>
       <name>dfs.replication</name>
       <value>3</value>
   </property>
   <property>
       <name>dfs.namenode.name.dir</name>
       <value>file:///usr/local/hadoop/hdfs/data</value>
   </property>
</configuration>

Edit etc/hadoop/mapred-site.xml on master node:
<configuration>
   <property>
       <name>mapreduce.jobtracker.address</name>
       <value>hadoop-master-server-ip:54311</value>
   </property>
   <property>
       <name>mapreduce.framework.name</name>
       <value>yarn</value>
   </property>
</configuration>

Edit etc/hadoop/yarn-site.xml on master node:
<configuration>
   <!-- Site specific YARN configuration properties -->
   <property>
       <name>yarn.nodemanager.aux-services</name>
       <value>mapreduce_shuffle</value>
   </property>
   <property>
<name> yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
<value>org.apache.hadoop.mapred.ShuffleHandler</value>
   </property>
   <property>
       <name>yarn.resourcemanager.hostname</name>
       <value>hadoop-master-server-ip</value>
   </property>
</configuration>

Create etc/hadoop/masters on Master node
Hadoop-master-server-ip

Edit etc/hadoop/workers on Master node
localhost

hadoop-worker-01-server-ip
hadoop-worker-02-server-ip
hadoop-worker-03-server-ip

Format hdfs on Master node
./bin/hdfs namenode -format

Start dfs on Master node: 
./sbin/start-dfs.sh

Start YARN on Master node: 
./sbin/start-yarn.sh

Check with jps

