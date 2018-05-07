class NodeClass:

    def __init__(self, i, j, sum_cost, depth, parent, algorithm):
        self.x = int(i)
        self.y = int(j)
        self.position = (int(i), int(j))
        self.sum_cost = float(sum_cost)
        self.parent = parent
        self.depth = int(depth)
        self.type = algorithm

    def __repr__(self):
    	return str(self.position)

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ","+ str(self.sum_cost) + "> "
   		# return "\n\nPosition: " + str(self.position) + "\nSum cost: " + str(self.sum_cost) + "\nParent: " + str(self.parent.position) + "\nDepth: " + str(self.depth)
        # return str(self.position) + " "
    
    def __eq__(self, other):
        return self.position == other.position