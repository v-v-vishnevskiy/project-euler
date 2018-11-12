#!/bin/bash

for key in "$@"
do
time $key -m unittest python/test.py
done
