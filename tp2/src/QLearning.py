from MDP import *
import random
import operator as op

class QLearningClass:

	def run(self, grid, terminals, alpha, gamma, N):

		mdp = MDPClass(terminals)
		gridMDP = GridMDPClass(grid, terminals)
		for x in range(gridMDP.rows):
			for y in range(gridMDP.cols):
				if grid[x][y] is not None:
					mdp.states.add((x, y))
					mdp.reward[x, y] = grid[x][y]
					mdp.state_actions.append((x,y,'acima'))
					mdp.state_actions.append((x,y,'abaixo'))
					mdp.state_actions.append((x,y,'direita'))
					mdp.state_actions.append((x,y,'esquerda'))


		# Inicializa Q com 0 para cada tupla (estado_x, estado_y, ação)
		Q = dict([(s_a, 0) for s_a in mdp.state_actions])

		episilon = 0.005
		# episode = 0

		current_state = random.sample(mdp.states,1)[0]
		# print("Episode: ", episode)
		
		for i in range(N):
			while current_state in mdp.terminals:
				# Final de um episodio		
				# episode += 1
				# print(alpha, episilon, i)

				# Decrementa alpha (diminuindo a taxa de aprendizado)
				alpha = abs(alpha - episilon)
				
				# Episilon atualizado assintoticamente
				episilon *= (i+1)/(i+2)

				# Começa novo episodio
				# print("Episode: ", episode)
				current_state = random.sample(mdp.states,1)[0]
			
			action = random.choice(list(mdp.actions(current_state).keys()))
			next_state = mdp.go(current_state,action)

			# Função Q-Learning 
			Q[current_state + (mdp.list_actions[action],)] = (1-alpha)*Q[current_state + (mdp.list_actions[action],)] + alpha*(mdp.R(next_state) + gamma*max([Q[current_state + (a,)] for a in list(mdp.list_actions.values())]))
			current_state = next_state

		#policy
		for state in mdp.states:
			# Cria um sub dicionario com cada ação para cada estado "state"
			subdict = {k:Q[k] for k in (state + (a,) for a in mdp.list_actions.values()) if k in Q}
			# print(subdict)

			#verifica qual o maior item no subdicionario e salva sua chave em maxi_key
			maxi_key = max(subdict.items(), key=op.itemgetter(1))[0]
			# print(maxi_key)

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