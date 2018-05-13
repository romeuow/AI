from BuildGraph import BuildGraphClass
from Queue import QueuePriorityClass
import sys
import math


class SearchClass:

    def search(self, problem, limit = math.inf):
        
        buildGraphClass = BuildGraphClass()
        frontier = QueuePriorityClass()
        explored = {}
        path = []
        nodes_expanded = 0
        
        frontier.add_item(problem.initial_state, problem.initial_state.function)
        if problem.initial_state.position == problem.goal_state.position:
            return problem.initial_state, nodes_expanded, path
        
        cutoff_ocurred = False
        while not frontier.is_empty():
            try:
                node = frontier.pop_item()
            except KeyError:
                break

            path.append(node)

            if node.position == problem.goal_state.position:
                self.clear(frontier, explored)
                return node, nodes_expanded, path
                
            if node.depth == limit:
                cutoff_ocurred = True
            
            childs = buildGraphClass.expand(node, problem.map_problem, frontier, explored, problem.goal_state)
            nodes_expanded += 1
            explored.update({node.position: node})
            
            for children in childs:
                if not frontier.contains(children.position):
                    frontier.add_item(children, children.function)
                else:
                    if limit != math.inf:
                        continue
                    else:
                        item = frontier.entry_finder[children.position][2]
                        if item.function > children.function:
                            frontier.add_item(children, children.function)
                            
        self.clear(frontier, explored)

        if cutoff_ocurred:
            return None, nodes_expanded, path
        else:
            problem.goal_state.failure = True
            problem.goal_state.g = math.inf
            return problem.goal_state, nodes_expanded, path

    def clear(self, frontier, explored):
        frontier.clear()
        explored.clear()
