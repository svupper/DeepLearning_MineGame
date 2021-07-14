import numpy as np


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Bomb = np.random.choice([0,1],p=[0.85,0.15])

        self.Neighboors = []
        self.revealed = False

    def __str__(self):
        i = 0
        for noud in self.Neighboors:
            if noud.Bomb == 1:
                i += 1
        return str(i)

    def __setitem__(self, b, x, y, n):
        self.Bomb = b
        self.x = x
        self.y = y
        self.Neighboors = n

    def __getitem__(self):
        # print(a)
        return self.Bomb, self.x, self.y, self.Neighboors

    def isrevealed(self):
        return self.revealed

    def reveal(self):
        self.revealed = True

    def hide(self):
        self.revealed = False

    def add_Neigh(self, n):
        self.Neighboors.append(n)

    def add_Neigh_List(self, nodes):
        self.Neighboors + nodes

    def isBomb(self):
        if self.Bomb:
            return True
        else:
            return False


class Maze:
    def __init__(self, n=5):
        self.Map = []
        self.N = n
        self.displayed = []
        self.create_Maze(n)
        self.stack_neigh()
        self.update_dispMap()

    def __str__(self):
        return self.displayed

    def __getitem__(self, pos):
        x, y = pos
        return self.Map[x][y]

    def __setitem__(self, x, y, node):
        self.Map[x][y] = node

    def setMap(self, map):
        self.Map = map
        self.N = len(map)
        self.stack_neigh()
        self.update_dispMap()

    def create_Maze(self, N):
        self.N = N
        for x in range(N):
            row = []
            for y in range(N):
                n = Node(x, y)
                row.append(n)
            self.Map.append(row)

    def stack_neigh(self):
        x = 0
        copy_map = []
        for i in range(self.N):
            row = self.Map[i].copy()
            copy_map.append(row)

        l = self.N - 1
        for row in copy_map:
            y = 0
            for node in row:
                for a in (-1, 0, 1):
                    for b in (-1, 0, 1):
                        if (a == 0) & (b == 0):
                            pass

                        elif (((x + a) < 0) | ((x + a) > l) | ((y + b) < 0) | ((y + b) > l) ):
                            pass
                        else:
                            n = self.Map[x + a][y + b]
                            node.add_Neigh(n)
                y += 1
            x += 1
        self.Map = copy_map

    def update_dispMap(self):
        self.displayed = []
        for row in self.Map:

            for node in row:
                if node.isrevealed():
                    self.displayed.append(str(node))
                else:
                    self.displayed.append('.')

    def print_Map(self):

        for row in self.displayed:
            print(row)

        print("----------------")

    def print_Bombs(self):
        for row in self.Map:
            r = []
            for col in row:
                r.append(col.Bomb)
            print(r)

    def revealCase(self, x, y):
        if not self.Map[x][y].isrevealed():
            self.Map[x][y].reveal()
            if str(self.Map[x][y]) == '0':
                origin = self.Map[x][y]
                for node in origin.Neighboors:
                    self.revealCase(node.x, node.y)

    def debugMap(self):
        self.Map = []
        for x in range(self.N):
            row = []
            for y in range(self.N):
                n = Node(x, y)
                if (y == (int(self.N/2))) & (x == (int(self.N/2))):
                    n.Bomb = 1
                else:
                    n.Bomb = 0
                row.append(n)
            self.Map.append(row)
        self.stack_neigh()
