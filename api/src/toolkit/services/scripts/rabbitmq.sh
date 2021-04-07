#!/bin/bash
# 安装erlang
apt-get install -y erlang

# 设置hostname为rabbitmq
echo 'rabbitmq' >/etc/hostname

# 安装rabbitmq
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
dpkg -i erlang-solutions_1.0_all.deb
wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | apt-key add -
echo "deb https://dl.bintray.com/rabbitmq/debian bionic main" | tee /etc/apt/sources.list.d/bintray.rabbitmq.list
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
