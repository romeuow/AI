#!/usr/bin/env bash
if [ $# -eq 6 ] && [ $6 = "1" ]; then
	MAPA=$(pwd)/$1
	python3 src/Main.py astar_manhattan $MAPA $2 $3 $4 $5
elif [ $# -eq 6 ] && [ $6 = "2" ]; then
	MAPA=$(pwd)/$1
	python3 src/Main.py astar_octile $MAPA $2 $3 $4 $5
else
	echo Incorrect parameters
fi
