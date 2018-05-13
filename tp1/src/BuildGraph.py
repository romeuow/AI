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
                        
                        current = NodeClass(i, j, node.depth + 1, node, node.type)

                        if node.type == 'ucs':
                            current.g = c.g(node, i, j)
                            current.function = current.g
                        elif node.type == 'bfs':
                            current.g = c.g(node, i, j)
                            current.h = c.manhattan(current, goal)
                            current.function = current.h
                        elif node.type == 'astar_manhattan':
                            current.g = c.g(node, i, j)
                            current.h = c.manhattan(current, goal)
                            current.function = current.g + current.h
                        elif node.type == 'astar_octile':
                            current.g = c.g(node, i, j)
                            current.h = c.octile(current, goal)
                            current.function = current.g + current.h
                            
                        valid_nodes_aux.update({(i,j): current})

                except KeyError:
                    pass
                except IndexError:
                    pass
                        
        # print(valid_nodes_aux)
        valid_nodes = valid_nodes_aux.copy()
        for item in valid_nodes_aux:
            # print(item)
            # print("Trabalhando no ", item, "\nHash = ", hash_map[item])
            if hash_map[item] == '@':                
                
                try:
                    del valid_nodes[item]
                except KeyError:
                    pass
                
                if item[0] == node.x: 
                    try:
                        # print("removendo na linha ")
                        del valid_nodes[item[0] + 1, item[1]]
                    except KeyError:
                        pass

                    try:
                        del valid_nodes[item[0] - 1, item[1]]
                    except KeyError:
                        pass                    

                elif item[1] == node.y:
                    
                    try:
                        # print("removendo na coluna ")
                        del valid_nodes[item[0], item[1] + 1]
                    except KeyError:
                        pass                    

                    try:
                        del valid_nodes[item[0], item[1] - 1]
                    except KeyError:
                        pass

        # print(list(valid_nodes.values()))
        return list(valid_nodes.values())

    # def print_map(self, hash_map):
    # 	out = open("mapaloco.map", 'w')
    # 	for i in range(255):
    # 		for j in range(255):
    # 				out.write(hash_map[(i,j)])
    # 		out.write('\n')
