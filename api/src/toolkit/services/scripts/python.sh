#!/bin/bash
add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update
sudo apt-get install python3.6

# 调整Python3的优先级，使得3.6优先级较高
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# 更改默认值，python默认为Python2，现在修改为Python3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
# 如果需要py3.6的开发环境：(因为需要python3.6m的so和/usr/include/python3.6m里的头文件)：
sudo apt-get install python3.6-dev

# pip 安装
sudo apt-get install python3-pip

# pip 相关设置
pip3 install --upgrade pip       #升级pip到最新版本
ln -s /usr/bin/pip3 /usr/bin/pip #创建pip3的软连接到pip
pip install virtualenv           #安装依赖包

# pip config
mkdir ~/.pip
touch ~/.pip/pip.conf
echo '[global]' >>~/.pip/pip.conf
echo 'index-url = https://pypi.tuna.tsinghua.edu.cn/simple' >>~/.pip/pip.conf

#
echo 'python env is ok'
exit 0
