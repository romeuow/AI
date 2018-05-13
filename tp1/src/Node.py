class NodeClass:

    def __init__(self, i, j, depth, parent, algorithm, g = 0, h = 0, function = 0, failure = False):
        self.x = int(i)
        self.y = int(j)
        self.position = (int(i), int(j))
        self.parent = parent
        self.depth = int(depth)
        self.type = algorithm
        self.failure = failure
        self.g = float(g)
        self.h = float(h)
        self.function = function

    def __repr__(self):
    	return str(self)

    def __str__(self):
        if self.type == 'bfs':
            return "<" + str(self.x) + "," + str(self.y) + ","+ str(self.g) + "> "    
        return "<" + str(self.x) + "," + str(self.y) + ","+ str(self.function) + "> "
   		# return "\n\nPosition: " + str(self.position) + "\nSum cost: " + str(self.sum_cost) + "\nParent: " + str(self.parent.position) + "\nDepth: " + str(self.depth) + "\nCost: " + str(self.cost)
        # return str(self.position) + " "
    
    def __eq__(self, other):
        return self.position == other.position

