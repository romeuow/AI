import random as r
import matplotlib.pyplot as plt
from Main import MainClass
from collections import OrderedDict




class TestsClass:

	
	path = "/home/romeu.oliveira/Documents/repos/AI/tp1/"

	m = MainClass()


	out = open(path + "out.txt", "w")
	
	out.seek(0)
	out.truncate()

	fig = plt.figure()
	fig.suptitle('Tests', fontsize=17)
	plt.xlabel('Time', fontsize=15)
	plt.ylabel('Nodes Expanded', fontsize=15)


	for i in range(50):
		out.writelines("\n======================================================================\n")
		out.writelines("\nTeste " +  str(i))
		start_x = r.randint(0, 255)
		start_y = r.randint(0, 255)
		goal_x = r.randint(0, 255)
		goal_y = r.randint(0, 255)
		out.writelines("\n(" + str(start_x) + "," + str(start_y) + ")   ->    (" + str(goal_x) + "," + str(goal_y) + ")\n")


		#result_ids, nodes_expanded_ids, total_time_ids = m.run('ids', start_x, start_y, goal_x, goal_y)


		result, nodes_expanded, total_time, explored = m.run('ucs', path + "map1.map", start_x, start_y, goal_x, goal_y)
		out.write("\n\nUCS\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
		out.write(str(result) + "\n" + str(nodes_expanded) + "\n")
		
		if result is not None:
			print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'ro', markersize=3.5, label='UCS algorithm')

		# out_bfs.write("<" + str(start_x) + "," + str(start_y) + ",0>\n")
		result, nodes_expanded, total_time, explored = m.run('bfs', path + "map1.map", start_x, start_y, goal_x, goal_y)
		out.write("\n\nBFS\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
		out.write(str(result) + "\n" + "str(nodes_expanded)" + "\n")

		if result is not None:
			print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'go', markersize=3.5, label='BFS algorithm')

		# out_astar_manhattan.write("<" + str(start_x) + "," + str(start_y) + ",0>\n")
		# result, nodes_expanded, total_time, explored = m.run('astar_manhattan', path + "map1.map", start_x, start_y, goal_x, goal_y)
		# out_astar_manhattan.write(str(result) + "\n\n" +  "\n\n\n\n")

		
		result, nodes_expanded, total_time, explored = m.run('astar_octile', path + "map1.map", start_x, start_y, goal_x, goal_y)
		out.write("\n\nA*\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
		out.write(str(result) + "\n" + "str(nodes_expanded)" + "\n")

		if result is not None:
			print(result, total_time, nodes_expanded)
			plt.plot(total_time, nodes_expanded, 'bo', markersize=3.5, label='A*(octile) algorithm')


	handles, labels = plt.gca().get_legend_handles_labels()
	by_label = OrderedDict(zip(labels, handles))
	plt.legend(by_label.values(), by_label.keys(), loc='best', prop={'size': 6})


	plt.grid()
	plt.show()
	out.close()	