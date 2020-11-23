# Created by wangmeng at 2020/11/23
set -e
apt update || true
# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
    echo "apt update failed but continue!"
fi
apt install privoxy -y
echo 'privoxy installed successfully'

sed -i 's/listen-address  localhost:8118/listen-address  0.0.0.0:8118/' /etc/privoxy/config
echo 'privoxy config updated'

systemctl restart privoxy.service
echo 'privoxy service restarted'
exit 0