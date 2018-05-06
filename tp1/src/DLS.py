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

    def __recursive_dls__(self, node, problem, limit, frontier, explored):
        # print("Explorados: ", str(explored.keys()))
        # print("Fronteira: ", frontier.keys())
        # print(node.position, "Solução??  ", node.position == problem.goal_state.position)
        # print("Chegou no fundo??  ", limit == 0)

        if node.position == problem.goal_state.position:
            return node
        elif limit == 0:
            return 'cutoff'
        
        else:
            cutoff_ocurred = False
            buildGraphClass = BuildGraphClass()
            # print("Expandir??  ", (node.position not in explored) and (node.position not in frontier))
            if (node.position not in explored) and (node.position not in frontier):
                explored.update({node.position: node})
                childs = buildGraphClass.expand(node, problem.map_problem)

                for child in childs:
                    frontier.update({child.position: child})
            elif not frontier:
                return 'failure'
            else: 
                return 'cutoff'            
            
            # print ("Filhos de  " + str(node.position) + "      " + childs.__str__())
            while frontier:
                item = frontier.popitem()
                # print(type(item[1]))
                # print("\n")
                result = self.__recursive_dls__(item[1], problem, limit - 1, frontier, explored)
                if result == 'cutoff':
                    cutoff_ocurred = True
                elif result == 'failure':
                    cutoff_ocurred = False
                    explored.update({item[1].position: item})
                else:
                    return result
            if cutoff_ocurred:
                return 'cutoff'
            else:
                return 'failure'

    def dls(self, problem, limit):
        # self.__verificar__(problem.map_problem)
        explored = {}
        frontier = {}
        result = self.__recursive_dls__(problem.initial_state, problem, limit, frontier, explored)
        return result, explored
