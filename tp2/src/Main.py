from BuildGrid import BuildGridClass
from QLearning import *
import sys
import time

class MainClass:
	
	start_time = time.time()
	buildGrid = BuildGridClass()
	q = QLearningClass()
	
	grid, terminals = buildGrid.build_grid(sys.argv[1])
	q.run(grid, terminals, float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]))
	# print(time.time() - start_time)