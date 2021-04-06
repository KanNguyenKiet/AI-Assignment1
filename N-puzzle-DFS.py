import sys
from state import State

class Solver:
	def __init__(self, state):
		self.size = int(state.n)
		self.begin_state = state
		self.begin_state.parent = State()
		self.final_state = []
		self.found = 0
		self.counter = 0
		print(len(self.begin_state.map))
		for i in range(self.size):
			x = []
			for j in range(self.size):
				x.append(i * self.size + j + 1)
			self.final_state.append(x)
		self.final_state[self.size - 1][self.size - 1] = -1


	def dfs(self, state):
		print(self.counter)
		self.counter += 1
		print(state)
		if state.map == self.final_state:
			self.found = 1
			return 1
		move_list = state.Move()
		# print("Number of possible move: ", len(move_list))
		# for move in move_list:
		# 	print(move)
		# 	print("-" * 10)
		for move in move_list:
			if move.map != state.parent.map:
				self.dfs(move)
				if self.found:	
					return 1

	def solve(self):
		if self.dfs(self.begin_state):
			print("Solution Found")


if __name__ == '__main__':
	size_of_puzzle = int(input("Enter size of puzzle: "))
	begin_state = State(size_of_puzzle)
	begin_state.input()
	begin_state.Move()
	# run = Solver(begin_state)
	# run.solve()


