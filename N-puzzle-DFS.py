class State:
    def __init__(self, _n):
	self.map = [[0] * int(_n)] * int(_n)
	self.n = int(_n)
	self.dx = [1, 0, -1, 0]
	self.dy = [0, -1, 0, 1]
	self.parent = State()

    def __int__(self, state):
	self.map = state


    def __init__(self):
	pass

           
    def input(self):
	for x in self.map:
	    x = [map(int, input().split())]

    def Move(self):
	x, y = 0, 0
	for i in range(self.n):
	    for j in range(self.n):
		if self.map[i][j] == -1:
		    x = i
		    y = j
		    break
	move_list = []
	for i in range(4):
	    if 0 <= x + self.dx[i] < self.n and 0 <= y + self.dy[i] < self.n:
		move_map = self.map
		move_map[x][y] = move_map[x + self.dx[i]][y + self.dy[i]]
		move_map[x + self.dx[i]][y + self.dy[i]] = -1
		move_list.append(move_map)
	return move_list



class Solver:
    def __init__(self, state):
	self.Env_State = Env()
	size = int(state.n)
	self.begin_state = state
        self.final_state = [[0] * size] * size
        self.found = 0
	print(len(self.final_state))
	for i in range(size):
	    for j in range(size):
		self.final_state[i][j] = i * size + j
	self.final_state[size - 1][size - 1] = -1

    def dfs(self, state):
        if state == self.final_state:
            self.found = 1
            return 1
	    move_list = state.Move()
            for move in move_list:
                if move != state.parent:
                    self.dfs(move)
                    if self.found:
                        return 1

    def solve(self):
	if self.dfs(self.begin_state):
	    print("Solution Found")


if __name__ == '__main__':
    size_of_puzzle = input("Enter size of puzzle: ")
    begin_state = State(size_of_puzzle)
    begin_state.input()
    run = Solver(begin_state)


