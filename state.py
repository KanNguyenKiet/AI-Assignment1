class State:
    def __init__(self, *args):
        # if len(args) == 0:
        #     self.map = []
        #     self.n = 0
        # elif isinstance(args[0], int):
        #     self.map = [] 
        #     self.n = int(args[0])
        # elif isinstance(args[0], list):
        #     self.map = args[0]
        #     self.n = len(args[0])
        self.map = []
        self.n = args[0]
        self.dx = [1, 0, -1, 0]
        self.dy = [0, -1, 0, 1]
        self.parent = None
           

    def input(self):
        for i in range(self.n):
            x = list(map(int, input().strip().split()))
            self.map.append(x)  


    def Move(self):
        # x, y = 0, 0
        # for i in range(self.n):
        #     for j in range(self.n):
        #         if self.map[i][j] == -1:
        #             x = i
        #             y = j	
        #             break
        move_list = []
        # print(x, y, sep = " ")
        x, y = 1, 1
        # for i in range(4):
        i = 1
        # if 0 <= x + self.dx[i] < self.n and 0 <= y + self.dy[i] < self.n:
        move_map = self.map.copy()
        print(move_map, self.map, sep = " ")
        # move_map[x][y] = move_map[x + self.dx[i]][y + self.dy[i]]
        # move_map[x + self.dx[i]][y + self.dy[i]] = -1
        move_map[0][0] = 129
        print(move_map, self.map, sep = " ")
        print(hex(id(move_map)), hex(id(self.map)), sep=" ")
        # move_map = State(move_map)
        # move_map.parent = state
        # move_list.append(move_map)
        return move_list

    def __str__(self):
        res = ""
        for i in range(self.n):
            for j in range(self.n):
                res += str(self.map[i][j]) + " "
            if i < self.n - 1:
                res += "\n"
        return res