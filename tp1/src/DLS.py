from BuildGraph import BuildGraphClass
import heapq as h
import sys


class DLSClass:
    sys.setrecursionlimit(20000)
    
    # def __verificar__(self, mapa):
    #     out = open("mapaloco.map", "w")
    #     for i in range(0,3):
    #         for j in range(0,256):
    #             out.write(str(mapa[(i,j)]))
    #     out.close()

    def __dlsRun__(self, node, problem, limit):
        
        buildGraphClass = BuildGraphClass()
        explored = {}
        frontier = {}

        while limit:
            explored.update({node.position: node})
            # print("Explorados: ", str(explored.keys()))
            childs = buildGraphClass.expand(node, problem.map_problem, frontier, explored)
            # print ("Filhos de  " + str(node.position) + "      " + childs.__str__())
            for child in childs:
                frontier.update({child.position: child})
            # print("Fronteira: ", frontier.keys())
            if not frontier:
                return 'failure', None
            item = frontier.popitem()
            node = item[1]
            limit -= 1
            # print(node.position, "Solução??  ", node.position == problem.goal_state.position)
            if node.position == problem.goal_state.position:
                explored.update({node.position: node})
                return node,explored
            # print(type(item[1]))
            # print("\n")
        # print("Chegou no fundo??  ", limit == 0)
        return 'cutoff', None

    def dls(self, problem, limit):
        # self.__verificar__(problem.map_problem)
        if problem.initial_state.position == problem.goal_state.position:
            return problem.initial_state, None
        if limit == 0:
            return 'cutoff', None        
        return self.__dlsRun__(problem.initial_state, problem, limit)