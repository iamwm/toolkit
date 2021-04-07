#!/bin/bash
echo "start generate http proxy configuration"
if [ ! -d /root/toolkit  ];then
  mkdir /root/toolkit
fi
cd /root/toolkit || exit
proxy_ip=$(/sbin/ifconfig -a | grep inet | grep -v 127.0.0.1 | grep -v inet6 | awk '{print $2}' | tr -d "addr:")
echo "generate profile file with:$proxy_ip"
cp /etc/profile ./
echo "export http_proxy=http://$proxy_ip:8118" >> ./profile
echo "export https_proxy=http://$proxy_ip:8118" >> ./profile
echo "profile file created"

echo "generate apt proxy conf file with:$proxy_ip"
echo "Acquire::http::Proxy http://$proxy_ip:8118/;" > ./98https-http-proxy
echo "Acquire::https::Proxy http://$proxy_ip:8118/;" >> ./98https-http-proxy

echo "http proxy file generated"
exit 0