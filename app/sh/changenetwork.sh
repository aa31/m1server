#! /usr/bin/env bash
ifconfig eth0 $1 netmask $2
route add default gw $3