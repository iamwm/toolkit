#!/bin/bash

## cfgsvr
### mongo1设置
mongo --port 27011 --eval "JSON.stringify(rs.initiate({_id:'cfgset',members:[{_id:1,host:'$1:27011'}]}))"
#mongo --port 27011 --eval "JSON.stringify(rs.add(\"192.168.0.119:27011\"))"

## shard1
### mongo1设置
mongo --port "$2" --eval "JSON.stringify(rs.initiate({_id:'shard1',members:[{_id:1,host:'$1:$2'}]}))"
#mongo --port 27001
#rs.initiate({_id:'shard1',members:[{_id:1,host:'192.168.0.78:27001'}]})
#rs.add("192.168.0.119:27001")

## shard2
### mongo2设置
mongo --port "$3" --eval "JSON.stringify(rs.initiate({_id:'shard2',members:[{_id:1,host:'$1:$3'}]}))"
#rs.initiate({_id:'shard2',members:[{_id:1,host:'192.168.0.119:27002'}]})
#rs.add("192.168.0.78:27002")
