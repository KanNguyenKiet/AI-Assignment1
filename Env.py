from state import State

class Env:
    def __init__(self, *args):
        self.visited = {}
        self.parent = {}

    def map_state(self, *args):
        map = []
        if isinstance(args[0], State):
            map = args[0].map
        else:
            map = args[0]
        res = ""
        for i in map:
            for x in i:
                res += str(x) + '.'
        return res

    def add_state(self, state):
        map = self.map_state(state)
        self.visited[map] = state.dir
        self.parent[map] = self.map_state(state.parent)

        
    def check_state(self, state):
        return self.map_state(state) in self.visited
