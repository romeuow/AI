class MDPClass:
	def __init__(self, terminals, gamma=.9):
		self.terminals = terminals
		self.gamma = gamma
		self.reward = {}
		self.states = set()
		self.list_actions = {(-1,0):'acima', (0,-1):'esquerda', (1,0):'abaixo', (0,1):'direita'}
		self.state_actions = []
		self.policy = {}

	def R(self, state):
		return self.reward[state]

	def actions(self, state):
		if state in self.terminals:
			return [None]
		else:
			return self.list_actions

	def go(self, state, direction):
		state1 = tuple(map(sum, zip(state, direction)))
		if state1 in self.states:
			return state1
		else:
			return state

class GridMDPClass:
	def __init__(self, grid, terminals):
		self.grid = grid
		self.rows = len(grid)
		self.cols = len(grid[0])
		
	def to_grid(self, mapping):
		grid_pi = []
		line_pi = []
		for x in range(self.rows):
			for y in range(self.cols):
				if self.grid[x][y] is None:
					line_pi.append('#')
				elif self.grid[x][y] == 10:
					line_pi.append('0')
				elif self.grid[x][y] == -10:
					line_pi.append('&')
				else:
					line_pi.append(mapping.get((x,y)))
			grid_pi.append(line_pi)
			line_pi = []
		return grid_pi

	def to_arrows(self, policy):
		chars = {'direita':'>', 'acima':'^', 'esquerda':'<', 'abaixo':'v', None: '.'}
		return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))