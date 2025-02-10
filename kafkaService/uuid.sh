#!/bin/bash 
cat /proc/sys/kernel/random/uuid | tr -d '-' | base64 | cut -b 1-22