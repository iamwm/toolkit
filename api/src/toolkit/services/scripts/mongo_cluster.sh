#!/bin/bash
# chkconfig: - 85 15
shard_seq_1="$1"
shard_seq_2="$2"
echo "shard$shard_seq_1 & shard$shard_seq_2 start configuration"

# install
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list

apt-get update

apt-get install -y mongodb-org=4.0.2 mongodb-org-server=4.0.2 mongodb-org-shell=4.0.2 mongodb-org-mongos=4.0.2 mongodb-org-tools=4.0.2

# 创建必要的文件夹
# 新建目录
mkdir -p /data/mongo/{mongos,mongo_cfgsvr,mongo_shard"$shard_seq_1",mongo_shard"$shard_seq_2"}/log/
mkdir -p /data/mongo/{mongo_cfgsvr,mongo_shard"$shard_seq_1",mongo_shard"$shard_seq_2"}/data/

# 环境变量设置
ulimit -f unlimited
ulimit -t unlimited
ulimit -v unlimited
ulimit -l unlimited
ulimit -n 64000
ulimit -m unlimited
ulimit -u 64000
CacheSizeGB=5

# config server & mongod
mongod --configsvr --dbpath /data/mongo/mongo_cfgsvr/data --logpath /data/mongo/mongo_cfgsvr/log/cfg.log --bind_ip 0.0.0.0 --port 27011 --replSet cfgset --fork
sleep 3
mongod --shardsvr --bind_ip 0.0.0.0 --port="$3" --replSet "shard$shard_seq_1" --dbpath "/data/mongo/mongo_shard$shard_seq_1/data" --logpath "/data/mongo/mongo_shard$shard_seq_1/log/shard$shard_seq_1.log" --wiredTigerCacheSizeGB=${CacheSizeGB} --fork
sleep 5
mongod --shardsvr --bind_ip 0.0.0.0 --port="$4" --replSet "shard$shard_seq_2" --dbpath "/data/mongo/mongo_shard$shard_seq_2/data" --logpath "/data/mongo/mongo_shard$shard_seq_2/log/shard$shard_seq_2.log" --wiredTigerCacheSizeGB=${CacheSizeGB} --fork
sleep 5
exit 0
