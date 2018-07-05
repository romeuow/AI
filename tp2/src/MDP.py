class MDPClass:
	"""A Markov Decision Process, defined by an initial state, transition model,
	and reward function. We also keep track of a gamma value, for use by
	algorithms. The transition model is represented somewhat differently from
	the text.  Instead of T(s, a, s') being  probability number for each
	state/action/state triplet, we instead have T(s, a) return a list of (p, s')
	pairs.  We also keep track of the possible states, terminal states, and
	actions for each state. [page 615]"""

	def __init__(self, terminals, gamma=.9):
		self.terminals = terminals
		self.gamma = gamma
		self.reward = {}
		self.states = set()
		self.list_actions = {(-1,0):'acima', (0,-1):'esquerda', (1,0):'abaixo', (0,1):'direita'}
		self.state_actions = []
		self.policy = {}


	def R(self, state):
		"Return a numeric reward for this state."
		return self.reward[state]

	def T(state, action):
		"""Transition model.  From a state and an action, return a list
		of (result-state, probability) pairs."""
		abstract

	def actions(self, state):
		"""Set of actions that can be performed in this state.  By default, a
		fixed list of actions, except for terminal states. Override this
		method if you need to specialize by state."""
		if state in self.terminals:
			return [None]
		else:
			return self.list_actions

	def go(self, state, direction):
		"Return the state that results from going in this direction."
		state1 = tuple(map(sum, zip(state, direction)))
		if state1 in self.states:
			return state1
		else:
			return state

class GridMDPClass:
	"""A two-dimensional grid MDP, as in [Figure 17.1].  All you have to do is
	specify the grid as a list of lists of rewards; use None for an obstacle
	(unreachable state).  Also, you should specify the terminal states.
	An action is an (x, y) unit vector; e.g. (1, 0) means move east."""
	def __init__(self, grid, terminals, gamma=.9):
		self.grid = grid
		self.rows = len(grid)
		self.cols = len(grid[0])
		
	def to_grid(self, mapping):
		"""Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
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
		chars = {(0, 1):'>', (-1, 0):'^', (0, -1):'<', (1, 0):'v', None: '.'}
		return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))