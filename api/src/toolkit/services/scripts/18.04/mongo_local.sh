#!/bin/bash
# chkconfig: - 85 15
wget -qO - https://www.mongodb.org/static/pgp/server-4.0.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu boinc/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list

apt-get update
apt-get install -y libcurl3
apt-get install -y mongodb-org=4.0.24 mongodb-org-server=4.0.24 mongodb-org-shell=4.0.24 mongodb-org-mongos=4.0.24 mongodb-org-tools=4.0.24
# 启动
sudo service mongod start #需要mongodb service
# 自启动设置
systemctl enable mongod.service
