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
                    if ((i,j) != node.position) and ((i,j) not in explored):
                        g = c.g(node, i, j)
                        current = NodeClass(i, j, g , node.depth + 1, node, node.type, 0)
                        h = c.octile(current, goal)
                        if node.type == 'ids':
                            valid_nodes_aux.update({(i,j): current})
                        elif node.type == 'ucs':
                            current.cost = g
                            valid_nodes_aux.update({(i,j): current})
                        elif node.type == 'bfs':
                            current.cost = h
                            valid_nodes_aux.update({(i,j): current})
                        elif node.type == 'astar':
                            current.cost = g + h
                            valid_nodes_aux.update({(i,j): current})
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