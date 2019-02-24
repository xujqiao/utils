awk '/Failed/{print $(NF-3)}' /var/log/secure | grep -v awk |sort|uniq -c|awk '{print $2"="$1;}' > /tmp/black.txt
DEFINE="5"
for i in `cat  /tmp/black.txt`; do
    IP=`echo $i |awk -F= '{print $1}'`
    NUM=`echo $i|awk -F= '{print $2}'`
    if [ $NUM -gt $DEFINE ]; then
        grep $IP /etc/hosts.deny > /dev/null
        if [ $? -gt 0 ];then
            echo "sshd:$IP:deny" >> /etc/hosts.deny
        fi
    fi
done
