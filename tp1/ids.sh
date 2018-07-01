#!/usr/bin/env bash
if [ $# -eq 5 ]; then
	MAPA=$(pwd)/$1
	python3 src/Main.py ids $MAPA $2 $3 $4 $5

else
	echo Incorrect parameters
fi