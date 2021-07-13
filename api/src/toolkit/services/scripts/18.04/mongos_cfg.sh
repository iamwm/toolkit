#!/bin/bash
# chkconfig: - 85 15
ulimit -f unlimited
ulimit -t unlimited
ulimit -v unlimited
ulimit -l unlimited
ulimit -n 64000
ulimit -m unlimited
ulimit -u 64000

mongos --bind_ip 0.0.0.0 --port 27010 --configdb cfgset/"$1":27011 --logpath /data/mongo/mongos/log/mongos.log --forks
mongo --port 27010 --eval "JSON.stringify(sh._adminCommand( { addShard : 'shard1/$1:27001' } , true ))"
mongo --port 27010 --eval "JSON.stringify(sh._adminCommand( { addShard : 'shard2/$1:27002' } , true ))"
