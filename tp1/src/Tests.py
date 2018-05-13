import random as r
import matplotlib.pyplot as plt
from Main import MainClass
from collections import OrderedDict




class TestsClass:

	# path = "/home/romeu.oliveira/Documents/repos/AI/tp1/"
	path = "C:\\Users\\romeu\\Documents\\repos\\AI\\tp1\\"

	out = open(path + "out.txt", "w")
	
	out.seek(0)
	out.truncate()

	fig = plt.figure()
	fig.suptitle('Tests', fontsize=17)
	plt.xlabel('Time', fontsize=15)
	plt.ylabel('Nodes Expanded', fontsize=15)

	valid_experiments = 0
	# sum_time_ids = .0
	sum_time_ucs = .0
	sum_time_bfs = .0
	# sum_time_astar_m = .0
	sum_time_astar_o = .0
	# sum_nodes_expanded_ids = .0
	sum_nodes_expanded_ucs = .0
	sum_nodes_expanded_bfs = .0
	# sum_nodes_expanded_astar_m = .0
	sum_nodes_expanded_astar_o = .0
	solution = .0
	# sum_distance_solution_ids = .0
	sum_distance_solution_bfs = .0
	# sum_distance_solution_astar_m = .0
	sum_distance_solution_astar_o = .0


	for i in range(60):

		out.writelines("\n======================================================================\n")
		out.writelines("\nTeste " +  str(i))
		print("\n\nTeste " +  str(i))
		start_x = r.randint(0, 255)
		start_y = r.randint(0, 255)
		goal_x = r.randint(0, 255)
		goal_y = r.randint(0, 255)
		out.writelines("\n(" + str(start_x) + "," + str(start_y) + ")   ->    (" + str(goal_x) + "," + str(goal_y) + ")\n")


		#result_ids, nodes_expanded_ids, total_time_ids = m.run('ids', start_x, start_y, goal_x, goal_y)

		result, nodes_expanded, total_time, explored = MainClass().run('ucs', path + "map1.map", start_x, start_y, goal_x, goal_y)

		
		if result is not None and not result.failure:
			out.write("\n\nUCS\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
			out.write(str(result) + "\n" + str(nodes_expanded) + "\n")
			valid_experiments += 1
			sum_time_ucs += total_time
			sum_nodes_expanded_ucs += nodes_expanded
			solution = result.function
			# print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'ro', markersize=3.5, label='UCS algorithm')
		else:
			continue

		result, nodes_expanded, total_time, explored = MainClass().run('bfs', path + "map1.map", start_x, start_y, goal_x, goal_y)

		if result is not None and not result.failure:
			out.write("\n\nBFS\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
			out.write(str(result) + "\n" + str(nodes_expanded) + "\n")
			sum_time_bfs += total_time
			sum_nodes_expanded_bfs += nodes_expanded
			sum_distance_solution_bfs += result.g - solution
			# print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'go', markersize=3.5, label='BFS algorithm')

		result, nodes_expanded, total_time, explored = MainClass().run('astar_octile', path + "map1.map", start_x, start_y, goal_x, goal_y)

		if result is not None and not result.failure:
			out.write("\n\nA* octile\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
			out.write(str(result) + "\n" + str(nodes_expanded) + "\n")
			sum_time_astar_o += total_time
			sum_nodes_expanded_astar_o += nodes_expanded
			sum_distance_solution_astar_o += result.function - solution
			# print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'bo', markersize=3.5, label='A*(octile) algorithm')

	out.write("================================Result=============================")
	out.write("\n\nDelta time ucs: " + str(sum_time_ucs/valid_experiments))
	out.write("\nDelta time bfs: " + str(sum_time_bfs/valid_experiments))
	out.write("\nDelta time astar_o: " + str(sum_time_astar_o/valid_experiments))
	out.write("\n\nDelta nodes_expanded ucs: " + str(sum_nodes_expanded_ucs/valid_experiments))
	out.write("\nDelta nodes_expanded bfs: " + str(sum_nodes_expanded_bfs/valid_experiments))
	out.write("\nDelta nodes_expanded astar_o: " + str(sum_nodes_expanded_astar_o/valid_experiments))
	out.write("\n\nDelta distance_solution_ucs: " + str(solution - solution))
	out.write("\nDelta distance_solution_bfs: " + str(sum_distance_solution_bfs/valid_experiments))
	out.write("\nDelta distance_solution_astar_o: " + str(sum_distance_solution_astar_o/valid_experiments))

	handles, labels = plt.gca().get_legend_handles_labels()
	by_label = OrderedDict(zip(labels, handles))
	plt.legend(by_label.values(), by_label.keys(), loc='best', prop={'size': 6})


	plt.grid()
	plt.show()
	out.close()	