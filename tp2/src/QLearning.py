from MDP import *
import random

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


		Q = dict([(s_a, 0) for s_a in mdp.state_actions])

		total_reward = 0
		episode = 0
		episilon = 0.0001
		policy = []


		current_state = random.sample(mdp.states,1)[0]
		# print("Episode: ", episode)
		
		for i in range(N):
		
			while current_state in mdp.terminals:
				# print("Total_reward: ", total_reward)
				episode += 1
				total_reward = 0
				alpha -= episilon
				# episilon *= 1/i+1
				# print("Episode: ", episode)
				current_state = random.sample(mdp.states,1)[0]
				# print("New random state: ", current_state)
			
			action = random.choice(list(mdp.actions(current_state).keys()))
			# print("Action: ", action)

			next_state = mdp.go(current_state,action)
			# print("Next state: ", next_state)
			total_reward += mdp.R(next_state)

		# for a in list(mdp.list_actions.values()):
		# 	print(Q[current_state + (a,)])
			Q[current_state + (mdp.list_actions[action],)] = (1-alpha)*Q[current_state + (mdp.list_actions[action],)] + alpha*(mdp.R(next_state) + gamma*max([Q[current_state + (a,)] for a in list(mdp.list_actions.values())]))
			current_state = next_state

		with open("q.txt", 'w') as f:
		    for key, value in Q.items():
		    	if (key[0],key[1]) not in mdp.terminals:
		        	f.write('%s,%s\n' % (str(key).strip('()').replace("'","").replace(" ", ""), value))

		#policy

		maxi = 0
		mini = 0
		for state in mdp.states:

			maxi = max([Q[state + (a,)] for a in list(mdp.list_actions.values())])
			mini = min([Q[state + (a,)] for a in list(mdp.list_actions.values())])

			if maxi != 0 and maxi != mini:
				policy.append(list(Q.keys())[list(Q.values()).index(maxi)])
			else:
				policy.append(state + ('acima',))

		# print(policy)

		for state_action in policy:
			mdp.policy.update({(state_action[0],state_action[1]): list(mdp.list_actions.keys())[list(mdp.list_actions.values()).index(state_action[2])]})
		
		with open("pi.txt", "w") as pi:

			# print(gridMDP.to_arrows(mdp.policy))
			for item in gridMDP.to_arrows(mdp.policy):
				pi.write("%s\n" % str(item).strip("[]").replace("'","").replace(", ",""))

		

		# pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
		

