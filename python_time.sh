#!/bin/bash

for key in "$@"
do
$key python/time_consumption.py
done
echo ""
