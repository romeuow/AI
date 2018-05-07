import math
import sys
import time
from BuildMap import BuildMapClass
from Problem import ProblemClass
from Node import NodeClass
from DLS import DLSClass

class IDSClass:

    def ids(self, problem):
        dlsClass = DLSClass()
        depth = 0
        while True:
            # print("\nIteração: ", depth)
            result, explored = dlsClass.dls(problem, depth)
            if result != 'cutoff':
                return result, explored
            depth += 1
