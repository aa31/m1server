#! /usr/bin/env bash
ifconfig eth0 arg1 = $1 netmask arg2 = $2
route add default gw arg3 = $3