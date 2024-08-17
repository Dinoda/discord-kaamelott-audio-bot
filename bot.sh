#!/bin/bash

LOGDIR=log/
LOG=${LOGDIR}log.txt

mkdir $LOGDIR > /dev/null 2> /dev/null

python3 main.py > $LOG 2> $LOG


