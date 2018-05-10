from BuildGraph import BuildGraphClass
from Queue import QueuePriorityClass
import sys


class SearchClass:

    def search(self, problem, limit, ids = False):
        
        buildGraphClass = BuildGraphClass()
        frontier = QueuePriorityClass()
        nodes_expanded = 0
        explored = {}
        frontier.add_item(problem.initial_state, problem.initial_state.cost)
        path = []

        if problem.initial_state.position == problem.goal_state.position:
            return problem.initial_state, nodes_expanded, path
        if limit == 0:
            return None, nodes_expanded, path

        cutoff_ocurred = False
        while not frontier.is_empty():
            node = frontier.pop_item()
            path.append(node)

            # print("Chegou no fundo??  ", limit == node.depth)
            if node.depth == limit:
                # print(node.position, "Solução??  ", node.position == problem.goal_state.position)
                cutoff_ocurred = True
                if node.position == problem.goal_state.position:
                    explored.update({node.position: node})
                    return node, nodes_expanded, path

            elif node.position == problem.goal_state.position:
                explored.update({node.position: node})
                return node, nodes_expanded, path
                
            else:
                explored.update({node.position: node})
                # print(node, end=' ')
                # print("Explorados: ", str(explored.keys()))
                childs = buildGraphClass.expand(node, problem.map_problem, frontier, explored, problem.goal_state)
                nodes_expanded += 1
                # print ("Filhos de  " + str(node.position) + "      " + childs.__str__())
                for children in childs:
                    if not frontier.contains(children.position):
                        frontier.add_item(children, children.cost)
                    else:
                        if(ids):
                            continue
                        else:
                            item = frontier.entry_finder[children.position][2]
                            # print(item.cost, children.cost)
                            if item.cost > children.cost:
                                # print("Removendo ", item, " com função =", item.cost)
                                # print("Adicionando ", children, " com função =", children.cost)
                                frontier.add_item(children, children.cost)
                                # item.sum_cost = children.sum_cost
                                # item.parent = node
                                # frontier.sort()
                                # item = frontier.entry_finder[children.position][2]
                                # print("mudou", item.cost)

                # print("Fronteira: ", frontier.__str__())
                
        if cutoff_ocurred:
            return None, nodes_expanded, path
        else:
            return 'failure', nodes_expanded, path