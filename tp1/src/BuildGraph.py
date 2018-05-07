from Node import NodeClass

class BuildGraphClass:

    @staticmethod
    def expand(node, hash_map, frontier, explored):

        valid_nodes = {}
        valid_nodes_aux = {}
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
                        valid_nodes_aux.update({(i,j): NodeClass(i, j, node.sum_cost + 1, node.depth + 1, node)})
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
                    
                else:
                    if (item[0] != node.x) and (item[1] != node.y):
                        valid_nodes[item].sum_cost += 0.5
            except KeyError:
                pass
            except IndexError:
                pass

        return list(valid_nodes.values())