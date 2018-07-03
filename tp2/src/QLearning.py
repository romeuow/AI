from MDP import *
import random

class QLearningClass:

	def run(self, grid, terminals, alpha, gamma, N):

		mdp = MDPClass(terminals)
		gridMDP = GridMDPClass(grid, terminals)
		for x in range(gridMDP.rows):
			for y in range(gridMDP.cols):
				mdp.reward[x, y] = grid[x][y]
				mdp.state_actions.append((x,y,'acima'))
				mdp.state_actions.append((x,y,'abaixo'))
				mdp.state_actions.append((x,y,'direita'))
				mdp.state_actions.append((x,y,'esquerda'))
				if grid[x][y] is not None:
					mdp.states.add((x, y))
		Q = dict([(s_a, 0) for s_a in mdp.state_actions])
		current_state = random.sample(mdp.states,1)[0]
		print(current_state)
		action = random.choice(list(mdp.actions(current_state).keys()))
		print(action)

		# while action is not None:
		next_state = mdp.go(current_state,action)
		print(next_state)

		# for a in list(mdp.list_actions.values()):
		# 	print(Q[current_state + (a,)])
		
		
		Q[current_state + (mdp.list_actions[action],)] = (1-alpha)*Q[current_state + (mdp.list_actions[action],)] + alpha*(mdp.R(next_state) + gamma*max([Q[current_state + (a,)] for a in list(mdp.list_actions.values())]))
		
		print(Q[current_state + (mdp.list_actions[action],)])
		# pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
		

