from BuildGraph import BuildGraphClass
from Queue import QueuePriorityClass
import sys


class DLSClass:
    sys.setrecursionlimit(20000)
    
    # def __verificar__(self, mapa):
    #     out = open("mapaloco.map", "w")
    #     for i in range(0,3):
    #         for j in range(0,256):
    #             out.write(str(mapa[(i,j)]))
    #     out.close()

    def __dlsRun__(self, problem, limit):
        
        buildGraphClass = BuildGraphClass()
        frontier = QueuePriorityClass()

        explored = {}
        frontier.add_item(problem.initial_state)
        if problem.initial_state.position == problem.goal_state.position:
            return problem.initial_state, None
        if limit == 0:
            return 'cutoff', None 

        cutoff_ocurred = False
        while frontier.is_empty():
            node = frontier.pop_item()
            # print("Chegou no fundo??  ", limit == node.depth)
            if node.depth == limit:
                # print(node.position, "Solução??  ", node.position == problem.goal_state.position)
                cutoff_ocurred = True
                if node.position == problem.goal_state.position:
                    explored.update({node.position: node})
                    return node, explored
                
            else:
                explored.update({node.position: node})
                # print("Explorados: ", str(explored.keys()))
                childs = buildGraphClass.expand(node, problem.map_problem, frontier, explored)
                # print ("Filhos de  " + str(node.position) + "      " + childs.__str__())
                for child in childs:
                    frontier.add_item(child)
                # print("Fronteira: ", frontier.__str__())
                
        if cutoff_ocurred:
            return 'cutoff', None
        else:
            return 'failure', None

    def dls(self, problem, limit):
        # self.__verificar__(problem.map_problem)
               
        return self.__dlsRun__(problem, limit)