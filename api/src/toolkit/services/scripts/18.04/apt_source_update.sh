#!/bin/bash
cp /etc/apt/sources.list /etc/apt/sources.list.backup
cat >/etc/apt/sources.list <<EOF
# deb cdrom:[Ubuntu 16.04 LTS _Xenial Xerus_ - Release amd64 (20160420.1)]/ boinc main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-security universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ boinc-security multiverse
EOF
echo 'replace apt source list'
apt-get update
apt-get install -y gcc g++ cmake
exit 0
