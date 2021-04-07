#!/bin/bash
apt-get remove --purge python-apt
apt-get install python-apt -f
cd /usr/lib/python3/dist-packages/ || exit 1
cp apt_pkg.cpython-3?m-x86_64-linux-gnu.so apt_pkg.cpython-36m-x86_64-linux-gnu.so
apt-get install python-software-properties
apt-get install software-properties-common
add-apt-repository ppa:vbernat/haproxy-1.8
apt update
apt install -y haproxy
haproxy -v
echo 'haproxy installed'
exit 0
