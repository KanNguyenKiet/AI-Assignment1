import sys
from state import State, map_check
from Env import Env

sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**5)

env = Env()

class Solver:
	def __init__(self, state):
		self.size = int(state.n)
		self.begin_state = state
		self.begin_state.parent = State()
		self.final_state = []
		self.counter = 0
		for i in range(self.size):
			x = []
			for j in range(self.size):
				x.append(i * self.size + j + 1)
			self.final_state.append(x)
		self.final_state[self.size - 1][self.size - 1] = 0


	def dfs(self, state):
		# self.counter += 1
		# print(self.counter)
		# print(state)
		# print('*' * 10)
		# print(state.parent)
		env.add_state(state)
		if map_check(state.map, self.final_state):
			return 1
		move_list = state.Move()
		# print("Number of possible move: ", len(move_list))
		# for move in move_list:
		# 	print(move)
		# 	print("-" * 10)
		for move in move_list:
			if not env.check_state(move):
				if self.dfs(move) == 1:
					return 1

	def solve(self):
		if self.dfs(self.begin_state):
			print("Solution Found")
		map = self.final_state
		map = env.map_state(map)
		step = []
		while map != env.map_state(begin_state):
			step.append(env.visited[map])
			map = env.parent[map]
		step.reverse()
		for i in step:
			print(i)
			

if __name__ == '__main__':
	size_of_puzzle = int(input())
	begin_state = State(size_of_puzzle)
	begin_state.input()
	run = Solver(begin_state)
	run.solve()


