from DLS import DLSClass

class IDSClass:

    def ids(self, problem):
        dlsClass = DLSClass()
        depth = 0
        result = None
        while result is None:
            # print("\nIteração: ", depth)
            result, explored = dlsClass.dls(problem, depth)
            depth += 1
        return result, explored
