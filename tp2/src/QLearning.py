from MDP import *
import random
import operator as op
import numpy as np

class QLearningClass:
	def run(self, grid, terminals, alpha, gamma, N):
		mdp = MDPClass(terminals)
		gridMDP = GridMDPClass(grid)
		for x in range(gridMDP.rows):
			for y in range(gridMDP.cols):
				if grid[x][y] is not None:
					mdp.states.add((x, y))
					mdp.reward[x, y] = grid[x][y]
					mdp.state_actions.append((x,y,'acima'))
					mdp.state_actions.append((x,y,'abaixo'))
					mdp.state_actions.append((x,y,'direita'))
					mdp.state_actions.append((x,y,'esquerda'))

		Q = dict([(s_a, 0) for s_a in mdp.state_actions])
		episilon = 1

		for i in range(N):
			current_state = random.sample(mdp.states,1)[0]
			while current_state not in mdp.terminals:
				# Cria um sub dicionario com as ações para current_state
				subdict = {k:Q[k] for k in (current_state + (a,) for a in mdp.list_actions.values()) if k in Q}
				# Verifica qual o maior item em subdict e salva sua chave em maxi_key
				maxi_key = max(subdict.items(), key=op.itemgetter(1))[0]
				if np.random.rand(1) < episilon:
					action = random.sample(mdp.list_actions.keys(), 1)[0]
				else:
					action = list(mdp.list_actions.keys())[list(mdp.list_actions.values()).index(maxi_key[2])]
				
				next_state = mdp.go(current_state,action)
				
				# Função Q-Learning 
				Q[current_state + (mdp.list_actions[action],)] = (1-alpha)*Q[current_state + (mdp.list_actions[action],)] + alpha*(mdp.R(next_state) + gamma*max([Q[next_state + (a,)] for a in list(mdp.list_actions.values())]))
				
				current_state = next_state
			episilon -= 1/N

		#policy
		for state in mdp.states:
			subdict = {k:Q[k] for k in (state + (a,) for a in mdp.list_actions.values()) if k in Q}
			maxi_key = max(subdict.items(), key=op.itemgetter(1))[0]
			mdp.policy.update({(maxi_key[0], maxi_key[1]): maxi_key[2]})
		
		# Arquivo q.txt
		with open("q.txt", 'w') as f:
		    for key, value in Q.items():
		    	if (key[0],key[1]) not in mdp.terminals:
		        	f.write('%s,%s\n' % (str(key).strip('()').replace("'","").replace(" ", ""), value))

		# Arquivo pi.txt		        	
		with open("pi.txt", "w") as pi:
			for item in gridMDP.to_arrows(mdp.policy):
				pi.write("%s\n" % str(item).strip("[]").replace("'","").replace(", ",""))