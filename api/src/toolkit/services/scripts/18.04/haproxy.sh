#!/bin/bash
apt-get remove -y --purge python-apt
apt-get install -y python-apt -f
cd /usr/lib/python3/dist-packages/ || exit 1
cp apt_pkg.cpython-3?m-x86_64-linux-gnu.so apt_pkg.cpython-36m-x86_64-linux-gnu.so
apt-get install -y python-software-properties
apt-get install -y software-properties-common
add-apt-repository -y ppa:vbernat/haproxy-1.8
apt update
apt install -y haproxy
haproxy -v
echo 'haproxy installed'
exit 0
