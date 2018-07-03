from BuildGrid import BuildGridClass
from Movement import MovementClass
from QLearning import *
import numpy as np
import sys

class MainClass:
	buildGrid = BuildGridClass()
	mv = MovementClass()
	grid, terminals, m, n = buildGrid.build_grid(sys.argv[1])
	q = QLearningClass()
	q.run(grid, terminals, float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]))
	


	# grid = np.array(grid)
	# print(np.array2string(grid, separator='\t'))
	# print(terminals)


	# #inicializar matriz Q mxn com zeros
	# Q = np.zeros((m,n), dtype=float)

	# print(Q)
	# mv.valid_movements(grid, 2, 3))


