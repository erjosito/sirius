#!/bin/bash
while true
do
    arp -d 172.18.1.1
    arp -d 172.18.1.254
    ping -c 1 172.18.1.1 >/dev/null
    ping -c 1 172.18.1.254 >/dev/null
    sleep 1
done
