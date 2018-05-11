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

	def __problem__(self, algorithm, mapa, initial_x, initial_y, goal_x, goal_y):
		return ProblemClass(BuildMapClass.build_map(mapa), NodeClass(initial_x, initial_y, 0, 0, None, algorithm, 0), NodeClass(goal_x, goal_y, 0, 0, math.inf, algorithm, 0))
    
	def run(self, algorithm, mapa, initial_x, initial_y, goal_x, goal_y):
		start_time = time.time()
		problem = self.__problem__(algorithm, mapa, initial_x, initial_y, goal_x, goal_y)
		
		try:
			if(problem.map_problem[problem.initial_state.position] == '@' or problem.map_problem[problem.goal_state.position] == '@'):
				# print('failure: goal or state closed')
				return None, 0 , time.time()-start_time, None
		except KeyError:
			# print('failure')
			return None, 0, time.time()-start_time, None
		
		search = SearchClass()
		if algorithm == 'ids':
			ids = IDSClass()
			result, nodes_expanded, explored = ids.ids(problem)
			total_time = time.time()-start_time
			return result, nodes_expanded, total_time, explored
		else:
			result, nodes_expanded, explored = search.search(problem, math.inf)
			total_time = time.time()-start_time
			# print(result, nodes_expanded)
			return result, nodes_expanded, total_time, explored

			
if len(sys.argv) == 7:
	MainClass().run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
else:
	print("Modo Teste / Quantidade incorreta de parametros.")