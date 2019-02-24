#/usr/bin/env sh
# $0 ssh_config_name /path/to/socket/file

HOSTNAME=$1
SOCKETFILE=$2

if [ ! -e  $SOCKETFILE ]; then
    echo "connecting $HOSTNAME .."
    ssh -fN $HOSTNAME
    if [ $? -ne 0 ]; then
        echo "failed to connect  $HOSTNAME" >&1
        exit 2
    fi
fi
