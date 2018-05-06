import math
import sys
import time
from BuildMap import BuildMapClass
from Problem import ProblemClass
from Node import NodeClass
from DLS import DLSClass

class IDSClass:

    def __ids__(problem):
        dlsClass = DLSClass()
        depth = 0
        while True:
            print("\nIteração: ", depth)
            result, explored = dlsClass.dls(problem, depth)
            if result != 'cutoff':
                return result, explored
            depth += 1

    if __name__ == '__main__':
        start_time = time.time()      
        problem = ProblemClass(BuildMapClass.build_map(), NodeClass(sys.argv[2], sys.argv[3], 0, 0, None), NodeClass(sys.argv[4], sys.argv[5], 0, 0, math.inf))
        try:
            if(problem.map_problem[problem.initial_state.position] == '@' or problem.map_problem[problem.goal_state.position] == '@'):
                print('failure')
                exit(0)
        except KeyError:
            print('failure')
            exit(0)
        result, explored = __ids__(problem)
        print(result)
        if explored is not None:
            for item in explored:
                print(explored[item], end='')
        print("\n\nElapsed time:", time.time()-start_time)
