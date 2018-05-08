import math

class CostClass:

	def g(self, node, i, j):
		if node.x == i or node.y == j:
			return node.sum_cost + 1
		else:
			return node.sum_cost + 1.5

	def manhattan(self, node, goal):
		return math.fabs(node.x - goal.x) + math.fabs(node.y - goal.y)

	def octile(self, node, goal):
		x = math.fabs(node.x - goal.x)
		y = math.fabs(node.y - goal.y)
		return max(x, y) + (0.5 * min(x, y))