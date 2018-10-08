#! /usr/bin/env bash
date -s $1
hwclock --systohc
hwclock -w
