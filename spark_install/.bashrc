#.bashrc
# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=
# User specific aliases and functions
module load gcc
module load slurm
module add prun

#JAVA
export JAVA_HOME=/var/scratch/ddps2212/jre1.8.0_351;
export PATH=/var/scratch/ddps2212/jre1.8.0_351/bin:/var/scratch/ddps2212/spark/bin:/bin:/cm/shared/apps/slurm/17.02.2/sbin:/cm/shared/apps/slurm/17.02.2/bin:/cm/local/apps/gcc/6.3.0/bin:/cm/shared/apps/torque/6.1.1/bin:/cm/shared/apps/torque/6.1.1/sbin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/sbin:/cm/local/apps/environment-modules/3.2.10/bin:/home/ddps2212/.local/bin:/home/ddps2212/bin:/home/ddps2212/.local/bin:/home/ddps2212/bin;
alias java="/var/scratch/ddps2212/jre1.8.0_351/bin/java"

#SPARK
export SPARK_HOME=/var/scratch/ddps2212/spark;
export PATH=/var/scratch/ddps2212/spark/bin:/var/scratch/ddps2212/spark/bin:/bin:/cm/shared/apps/slurm/17.02.2/sbin:/cm/shared/apps/slurm/17.02.2/bin:/cm/local/apps/gcc/6.3.0/bin:/cm/shared/apps/torque/6.1.1/bin:/cm/shared/apps/torque/6.1.1/sbin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/sbin:/cm/local/apps/environment-modules/3.2.10/bin:/home/ddps2212/.local/bin:/home/ddps2212/bin:/home/ddps2212/.local/bin:/home/ddps2212/bin;
