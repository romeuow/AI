class ProblemClass:

    def __init__(self, map_problem, initial_state, goal_state):
        self.map_problem = map_problem
        self.initial_state = initial_state
        self.goal_state = goal_state

    def __repr__(self):
    	return "ProblemClass()"

    def __str__(self):
    	return ("Initial State = " + str(self.initial_state) + "Goal state = " + str(self.goal_state))

    def __eq__(self, other):
    	return self.hash == other.hash
    
    def __hash__(self):
    	return self.hash