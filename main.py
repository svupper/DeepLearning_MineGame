# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Bomb = random.randint(0, 1)
        self.Neighboors = []

    def __str__(self):
        i = 0
        for node in self.Neighboors:
            if node.Bomb == 1:
                i += 1
        return i

    def __setitem__(self, b, x, y, n):
        self.Bomb = b
        self.x = x
        self.y = y
        self.Neighboors = n

    def __getitem__(self):
        return self.Bomb, self.x, self.y, self.Neighboors

    def add_Neigh(self, node):
        self.Neighboors.append(node)

    def add_Neigh_List(self, nodes):
        self.Neighboors + nodes

class Maze:
    def __init__(self, N=5):
        self.Map = []
        self.displayed = []
        self.create_MazeBomb(N)
        self.create_flip()

    def __str__(self):
        return self.displayed

    def __getitem__(self, x, y):
        return self.Map[x][y]

    def __setitem__(self,x,y):
        node = self.Map[x][y]
        self.displayed[x][y] = node

    def create_MazeBomb(self,N):
        self.N = N
        for x in range(N):
            row = []
            for y in range(N):
                n = Node(x, y)
                row.append(n)
            self.Map.append(row)

    def create_flip(self):
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
            r=[]
            for col in row:
                r.append(col.Bomb)
            print(r)

    def revealCase(self,x,y):
        for row in self.Map:
            r=[]
            j=0
            for col in row:

                print(row)
                print(j)
                if ((row==x) & (col==y)):
                    r.append(self.Map[x][y].Bomb)
                    print("ezan")
                else:
                    r.append('.')
            print(r)



if __name__ == '__main__':
    m = Maze()
    #m.create_MazeBomb(5)
    #m.create_flip()
    #m.print_Map()
    #m.revealCase(1,1)
    #m.flip_Maze()
    #while(1):
        #wait user move
        #m.print_Map()
        #reveal case
        #check if bomb
        #ifBomb
            #endgame
        #else
            #continue
