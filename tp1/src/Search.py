from BuildGraph import BuildGraphClass
from Queue import QueuePriorityClass
import sys
import math


class SearchClass:

    def search(self, problem, limit = math.inf):
        
        buildGraphClass = BuildGraphClass()
        frontier = QueuePriorityClass()
        explored = {}
        path = []
        nodes_expanded = 0
        
        frontier.add_item(problem.initial_state, problem.initial_state.function)
        if problem.initial_state.position == problem.goal_state.position:
            return problem.initial_state, nodes_expanded, path
        
        cutoff_ocurred = False
        # print(frontier)
        while not frontier.is_empty():
            try:
                node = frontier.pop_item()
            except KeyError:
                break

            # print("Vez de: ", node)
            path.append(node)

            if node.position == problem.goal_state.position:
                # print("Solução! ", node.position == problem.goal_state.position)
                self.clear(frontier, explored)
                return node, nodes_expanded, path
                
            # print("Chegou no fundo??  ", limit == node.depth)
            if node.depth == limit:
                cutoff_ocurred = True
            
            # print(node, end=' ')
            # print("Explorados: ", str(explored.keys()))
            childs = buildGraphClass.expand(node, problem.map_problem, frontier, explored, problem.goal_state)
            nodes_expanded += 1
            explored.update({node.position: node})
            # print ("Filhos de  " + str(node.position) + "      " + str(childs))
            for children in childs:
                # if(node.type == 'astar_octile'):
                #     print("filho")

                if not frontier.contains(children.position):
                    frontier.add_item(children, children.function)
                    # if node.type == 'astar_octile':
                    #     print(children.position, " NAO ta na fronteira")
                    # print(frontier)
                else:
                    if limit != math.inf:
                        continue
                    else:
                        item = frontier.entry_finder[children.position][2]
                        # if(node.type == 'astar_octile'):
                            # print("\n\n", item, " ta na fronteira.\nFronteira: ", frontier.entry_finder, "\nNós expandidos: ", nodes_expanded) 
                        # print(item.cost, children.cost)
                        if item.function > children.function:
                            # print("Removendo ", item, " com função =", item.cost)
                            # print("Adicionando ", children, " com função =", children.cost)
                            frontier.add_item(children, children.function)
                            # item = children
                            # frontier.sort()
                            # item = frontier.entry_finder[children.position][2]
                            # print("mudou", item.cost)

                # print("Fronteira: ", frontier.__str__())
        
        # print("Acabou a fronteira")

        self.clear(frontier, explored)

        if cutoff_ocurred:
            return None, nodes_expanded, path
        else:
            problem.goal_state.failure = True
            problem.goal_state.function = math.inf
            return problem.goal_state, nodes_expanded, path

    def clear(self, frontier, explored):
        frontier.clear()
        explored.clear()
