import random


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Bomb = random.randint(0, 1)
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

    def __getitem__(self, a):
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


class Maze:
    def __init__(self, n=5):
        self.Map = []
        self.N = n
        self.displayed = []
        self.create_MazeBomb(n)
        self.create_dispMap()
        self.stack_neigh()

    def __str__(self):
        return self.displayed

    def __getitem__(self, pos):
        x, y = pos
        return self.Map[x][y]

    def __setitem__(self, x, y):
        node = self.Map[x][y]
        self.displayed[x][y] = node

    def create_MazeBomb(self, N):
        self.N = N
        for x in range(N):
            row = []
            for y in range(N):
                n = Node(x, y)
                row.append(n)
            self.Map.append(row)

    def stack_neigh(self):
        x = 0
        mapo = []
        for i in range(self.N):
            row = self.Map[i].copy()
            mapo.append(row)

        l = self.N - 1
        for row in mapo:
            y = 0
            for node in row:
                for a in (-1, 0, 1):
                    for b in (-1, 0, 1):
                        if (a == 0) & (b == 0):
                            pass
                        elif (((x + a) < 0) | ((x + a) > l) | ((y + a) < 0) | ((y + a) > l) | ((x + b) < 0) | (
                                (x + b) > l) | ((y + b) < 0) | ((y + b) > l)):
                            pass
                        else:
                            n = self.Map[x + a][y + b]
                            node.add_Neigh(n)
                y += 1
            x += 1
        self.Map = mapo

    def create_dispMap(self):
        for row in self.Map:
            r = []
            for col in row:
                r.append(".")
            self.displayed.append(r)

    def print_Map(self):
        for row in self.displayed:
            print(row)

    def print_realMap(self):
        for row in self.Map:
            r = []
            for col in row:
                r.append(col.Bomb)
            print(r)

    def revealCase(self, x, y):
        #i = 0
        #for row in self.Map:
            #j = 0
            #for nod in row:
                #if ((i == x) & (j == y)):
        if self.displayed[x][y].__eq__('.'):
            self.displayed[x][y] = self.Map[x][y].__str__()
            # self.Map[x][y].reveal()
            if self.displayed[x][y].__eq__('0'):
                nod = self.Map[x][y]
                for node in nod.Neighboors:
                    self.revealCase(node.x, node.y)
                #j += 1
            #i += 1
        self.print_Map()
        print("----------------")

    def debugMap(self):
        self.Map = []
        for x in range(self.N):
            row = []
            for y in range(self.N):
                n = Node(x, y)
                if (y == 2) & (x == 2):
                    n.Bomb = 1
                else:
                    n.Bomb = 0
                row.append(n)
            self.Map.append(row)
        self.stack_neigh()


if __name__ == '__main__':
    debug = True
    m = Maze()
    if debug:
        m.debugMap()

    m.print_realMap()
    m.revealCase(0, 0)
    # for i in range(5):
    #     for j in range(5):
    #         m.revealCase(i, j)

    # while(1):
    # wait user move
    # m.print_Map()
    # reveal case
    # check if bomb
    # ifBomb
    # endgame
    # else
    # continue
