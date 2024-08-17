#!/bin/bash

LOGDIR=log/
LOG=${LOGDIR}log.txt

mkdir $LOGDIR

python3 main.py > $LOG 2> $LOG


