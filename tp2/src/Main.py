from BuildGrid import BuildGridClass
from QLearning import *
import sys

class MainClass:
	buildGrid = BuildGridClass()
	grid, terminals, m, n = buildGrid.build_grid(sys.argv[1])
	q = QLearningClass()
	q.run(grid, terminals, float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]))
	

