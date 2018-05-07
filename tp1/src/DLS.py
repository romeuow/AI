from Search import SearchClass

class DLSClass:

    def dls(self, problem, limit):
        searchClass = SearchClass()               
        return searchClass.search(problem, limit, True)