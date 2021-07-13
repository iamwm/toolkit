#!/bin/bash
# 安装erlang
apt-get install -y erlang
apt-get install apt-transport-https
# 设置hostname为rabbitmq
echo 'rabbitmq' >/etc/hostname

# 安装rabbitmq
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
dpkg -i erlang-solutions_1.0_all.deb

curl -1sLf 'https://packagecloud.io/rabbitmq/rabbitmq-server/gpgkey' | sudo apt-key add -
tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
## Provides modern Erlang/OTP releases
##
deb http://ppa.launchpad.net/rabbitmq/rabbitmq-erlang/ubuntu bionic main
deb-src http://ppa.launchpad.net/rabbitmq/rabbitmq-erlang/ubuntu bionic main

## Provides RabbitMQ
##
deb https://packagecloud.io/rabbitmq/rabbitmq-server/ubuntu/ bionic main
deb-src https://packagecloud.io/rabbitmq/rabbitmq-server/ubuntu/ bionic main
EOF
apt-get update
apt-get install -y rabbitmq-server

# 设置用户名和密码
rabbitmqctl add_user rabbitmq realtech@123
rabbitmqctl set_user_tags rabbitmq administrator
rabbitmqctl set_permissions rabbitmq ".*" ".*" ".*"

# 开启mqtt插件
rabbitmq-plugins enable rabbitmq_mqtt
# 开启web监控页面
rabbitmq-plugins enable rabbitmq_management
service rabbitmq-server restart