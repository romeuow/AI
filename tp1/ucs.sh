#!/usr/bin/env bash
if [ $# -eq 5 ]; then
	MAPA=$(pwd)/$1
	python3 src/Main.py ucs $MAPA $2 $3 $4 $5 $6

else
	echo Incorrect parameters
fi