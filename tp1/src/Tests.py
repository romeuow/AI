import random as r
from Main import MainClass

class TestsClass:

	path = "/home/romeu.oliveira/Documents/repos/AI/tp1/"

	m = MainClass()


	out = open(path + "out.txt", "w")
	
	out.seek(0)
	out.truncate()

	for i in range(30):
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

		# out_bfs.write("<" + str(start_x) + "," + str(start_y) + ",0>\n")
		# result, nodes_expanded, total_time, explored = m.run('bfs', path + "map1.map", start_x, start_y, goal_x, goal_y)
		# out_bfs.write(str(result) + "\n\n" +  "\n\n\n\n")

		# out_astar_manhattan.write("<" + str(start_x) + "," + str(start_y) + ",0>\n")
		# result, nodes_expanded, total_time, explored = m.run('astar_manhattan', path + "map1.map", start_x, start_y, goal_x, goal_y)
		# out_astar_manhattan.write(str(result) + "\n\n" +  "\n\n\n\n")

		
		result, nodes_expanded, total_time, explored = m.run('astar_octile', path + "map1.map", start_x, start_y, goal_x, goal_y)
		out.write("\n\nA*\n<" + str(start_x) + "," + str(start_y) + ",0>\n")
		out.write(str(result) + "\n" + "str(nodes_expanded)" + "\n")

		# if explored is not None:
		# 	for item in explored:
		# 		out_astar_octile.write(str(item) + " ")
		# out_astar_octile.write("\n\n")

	out.close()	