from Node import NodeClass

class BuildGraphClass:

    @staticmethod
    def expand(node, hash_map):

        valid_nodes = []
        
        try:
            if hash_map[(node.x, node.y - 1)] == '.' and (node.parent is None or ((node.x, node.y - 1) != node.parent.position)):
                valid_nodes.append(NodeClass(node.x, node.y - 1, node.sum_cost + 1, node.depth + 1, node))
                if hash_map[(node.x - 1, node.y - 1)] == '.'  and (node.parent is None or ((node.x - 1, node.y - 1) != node.parent.position)):
                    valid_nodes.append(NodeClass(node.x - 1, node.y - 1, node.sum_cost + 1.5, node.depth + 1, node))
        except KeyError:
            pass
        except IndexError:
            pass

        try:
            if hash_map[(node.x - 1, node.y)] == '.' and (node.parent is None or ((node.x - 1, node.y) != node.parent.position)):
                valid_nodes.append(NodeClass(node.x - 1, node.y, node.sum_cost + 1, node.depth + 1, node))
                if hash_map[(node.x - 1, node.y + 1)] == '.' and (node.parent is None or ((node.x - 1, node.y + 1) != node.parent.position)):
                    valid_nodes.append(NodeClass(node.x - 1, node.y + 1, node.sum_cost + 1.5, node.depth + 1, node))
            elif hash_map[(node.x - 1, node.y)] == '@' and not (valid_nodes[-1].x == node.x or valid_nodes[-1].y == node.y):
                valid_nodes.pop()
        except KeyError:
            pass
        except IndexError:
            pass

        try:
            if hash_map[(node.x, node.y + 1)] == '.' and (node.parent is None or ((node.x, node.y + 1) != node.parent.position)):
                valid_nodes.append(NodeClass(node.x, node.y + 1, node.sum_cost + 1, node.depth + 1, node))
                if hash_map[(node.x + 1, node.y + 1)] == '.' and (node.parent is None or ((node.x + 1, node.y + 1) != node.parent.position)):
                    valid_nodes.append(NodeClass(node.x + 1, node.y + 1, node.sum_cost + 1.5, node.depth + 1, node))
            elif hash_map[(node.x, node.y + 1)] == '@' and not (valid_nodes[-1].x == node.x or valid_nodes[-1].y == node.y):
                valid_nodes.pop()
        except KeyError:
            pass
        except IndexError:
            pass

        try:
            if hash_map[(node.x + 1, node.y)] == '.' and (node.parent is None or ((node.x + 1, node.y) != node.parent.position)):
                valid_nodes.append(NodeClass(node.x + 1, node.y, node.sum_cost + 1, node.depth + 1, node))
                if hash_map[(node.x + 1, node.y - 1)] == '.' and (node.parent is None or ((node.x + 1, node.y - 1) != node.parent.position)):
                    valid_nodes.append(NodeClass(node.x + 1, node.y - 1, node.sum_cost + 1.5, node.depth + 1, node))
            elif hash_map[(node.x + 1, node.y)] == '@' and not (valid_nodes[-1].x == node.x or valid_nodes[-1].y == node.y):
                valid_nodes.pop()
        except KeyError:
            pass
        except IndexError:
            pass

        try:
            if hash_map[(node.x, node.y-1)] == '@' and not (valid_nodes[-1].x == node.x or valid_nodes[-1].y == node.y):
                valid_nodes.pop()
        except KeyError:
            pass
        except IndexError:
            pass

        return valid_nodes