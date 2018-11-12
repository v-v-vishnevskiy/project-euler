#!/bin/bash

for key in "$@"
do
time $key python/time_consumption.py
done
echo ""
