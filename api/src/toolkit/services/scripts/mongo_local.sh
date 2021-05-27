#!/bin/bash
# chkconfig: - 85 15

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list

apt-get update
apt-get install -y libcurl3
apt-get install -y mongodb-org=4.0.24 mongodb-org-server=4.0.24 mongodb-org-shell=4.0.24 mongodb-org-mongos=4.0.24 mongodb-org-tools=4.0.24
# 启动
sudo service mongod start #需要mongodb service
# 自启动设置
systemctl enable mongod.service
