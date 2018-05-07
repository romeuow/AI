#Main
import sys
import time
import math
from IDS import IDSClass
from Search import SearchClass
from Problem import ProblemClass
from BuildMap import BuildMapClass
from Node import NodeClass

class MainClass:
    
	if __name__ == '__main__':
		start_time = time.time()      
		problem = ProblemClass(BuildMapClass.build_map(), NodeClass(sys.argv[3], sys.argv[4], 0, 0, None), NodeClass(sys.argv[5], sys.argv[6], 0, 0, math.inf))
		try:
			if(problem.map_problem[problem.initial_state.position] == '@' or problem.map_problem[problem.goal_state.position] == '@'):
				print('failure')
				exit(0)
		except KeyError:
			print('failure')
			exit(0)
		
		search = SearchClass()
		if sys.argv[1] == 'ids':
			ids = IDSClass()
			result, explored = ids.ids(problem)
			print(result)
		elif sys.argv[1] == 'ucs':
			result, explored = search.search(problem, math.inf)
			print(result)
		elif sys.argv[1] == 'bfs':
			result, explored = search.search(problem, math.inf)
		# if explored is not None:
		#     for item in explored:
		#         print(explored[item], end='')
		print("\n\nElapsed time:", time.time()-start_time)