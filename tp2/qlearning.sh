#!/usr/bin/env bash
if [ $# -eq 4 ]; then
	MUNDO=$(pwd)/$1
	python3 src/Main.py $MUNDO $2 $3 $4 
else
	echo Incorrect parameters
fi
