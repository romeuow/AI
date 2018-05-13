#Main
import sys
import time
import math
from Search import SearchClass
from Problem import ProblemClass
from BuildMap import BuildMapClass
from Node import NodeClass

class MainClass:

	def __init__(self):
		pass

	def __problem__(self, algorithm, mapa, initial_x, initial_y, goal_x, goal_y):
		return ProblemClass(BuildMapClass.build_map(mapa), NodeClass(initial_x, initial_y,  0, None, algorithm), NodeClass(goal_x, goal_y, 0, None, algorithm))
    
	def run(self, algorithm, mapa, initial_x, initial_y, goal_x, goal_y):
		out = open('out_tp1.txt', 'w')
		out.seek(0)
		out.truncate()

		start_time = time.time()
		problem = self.__problem__(algorithm, mapa, initial_x, initial_y, goal_x, goal_y)
		
		try:
			if(problem.map_problem[problem.initial_state.position] == '@' or problem.map_problem[problem.goal_state.position] == '@'):
				problem.goal_state.failure = True
				problem.goal_state.g = math.inf
				print("Initial or Goal state inaccessible")
				print("Output: ", out.name)
				out.write(str(problem.initial_state) + '\n' + str(problem.goal_state) + "\n\n")
				out.close()
				return problem.goal_state, 0 , time.time()-start_time, None
		except KeyError:
			problem.goal_state.failure = True
			problem.goal_state.g = math.inf
			print("Initial or Goal state inaccessible")
			print("Output: ", out.name)
			out.write(str(problem.initial_state) + '\n' + str(problem.goal_state) + "\n\n")
			out.close()
			return problem.goal_state, 0, time.time()-start_time, None
		
		search = SearchClass()
		if algorithm == 'ids':
			limit = 0
			result = None
			while result is None:
				result, nodes_expanded, path = search.search(problem, limit)
				limit += 1
			total_time = time.time()-start_time
			print("Output: ", out.name)
			out.write(str(problem.initial_state) + '\n' + str(result) + "\n\n" + str(path))
			out.close()
			return result, nodes_expanded, total_time, path
		else:
			result, nodes_expanded, path = search.search(problem)
			total_time = time.time()-start_time
			print("Output: ", out.name)
			out.write(str(problem.initial_state) + '\n' + str(result) + "\n\n" + str(path))
			out.close()
			return result, nodes_expanded, total_time, path

if __name__ == '__main__':
	if len(sys.argv) == 7:
		MainClass().run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	else:
		print("Quantidade incorreta de parametros.")
		