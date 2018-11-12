#!/bin/bash

for key in "$@"
do
$key -m unittest python/test.py
done
