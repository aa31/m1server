#! /usr/bin/env bash

echo "this is a test shell with arguments"
ifconfig eth0 arg1 = $1 netmask arg2 = $2
route add default gw arg3 = $3