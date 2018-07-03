class BuildGridClass:
	def build_grid(self, inp):
		world = open(inp, "r")
		line_num = int(world.read(2))
		column_num = int(world.read(2))
		
		grid = []
		line = []
		terminals = []
		reward = None
		for i in range(0, line_num):
			for j in range(0, column_num):
				element = world.read(1)
				if element == '-':
					reward = -1
				elif element == '&':
					reward = -10
					terminals.append((i,j))
				elif element == '0':
					reward = 10
					terminals.append((i,j))
				line.append(reward)
				reward = None
			world.read(1)
			grid.append(line)
			line = []
		return grid, terminals, line_num, column_num