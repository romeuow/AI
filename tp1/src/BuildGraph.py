from Node import NodeClass
from Cost import CostClass

class BuildGraphClass:

    @staticmethod
    def expand(node, hash_map, frontier, explored, goal):

        valid_nodes = {}
        valid_nodes_aux = {}

        c = CostClass()

        for i in range(node.x - 1, node.x + 2):
            for j in range(node.y - 1, node.y + 2):
                try:
                    hash_map[(i,j)] == ('.' or '@')
                    # print((i,j), node.position)
                    # print(node.parent )
                    # print((i,j) not in explored)
                    # print((i,j) not in frontier)
                    # print("\n")                    
                    if ((i,j) != node.position) and (node.parent is None or (i,j) != node.parent.position) and ((i,j) not in explored):
                        if node.type == 'ids':
                            valid_nodes_aux.update({(i,j): NodeClass(i, j, node.sum_cost + c.g(node, i, j) , node.depth + 1, node, 'ids')})
                        elif node.type == 'ucs':
                            valid_nodes_aux.update({(i,j): NodeClass(i, j, node.sum_cost + c.g(node, i, j) , node.depth + 1, node, 'ucs')})
                        elif node.type == 'bfs':
                            valid_nodes_aux.update({(i,j): NodeClass(i, j, node.sum_cost + c.manhattan(node, goal) , node.depth + 1, node, 'bfs')})
                        elif node.type == 'astar':
                            valid_nodes_aux.update({(i,j): NodeClass(i, j, node.sum_cost + c.g(node, i, j) + c.manhattan(node, goal) , node.depth + 1, node, 'astar')})
                except KeyError:
                    pass
                except IndexError:
                    pass
                        
        # print(valid_nodes_aux)
        valid_nodes = valid_nodes_aux.copy()
        for item in valid_nodes_aux:
            try:
                # print("Trabalhando no ", item, "\nHash = ", hash_map[item])
                if hash_map[item] == '@':                
                    del valid_nodes[item]
                    if item[0] == node.x:
                        del valid_nodes[(item[0] + 1, item[1])]
                        del valid_nodes[(item[0] - 1, item[1])]

                    elif item[1] == node.y:
                        del valid_nodes[(item[0], item[1] + 1)]
                        del valid_nodes[(item[0], item[1] - 1)]                
            except KeyError:
                pass
            except IndexError:
                pass

        return list(valid_nodes.values())