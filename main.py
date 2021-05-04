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
        for noud in self.Neighboors:
            if noud.Bomb == 1:
                i += 1
        if i>0:
            return str(i)
        else:
            return '.' #reveal neighboor

    def __setitem__(self, b, x, y, n):
        self.Bomb = b
        self.x = x
        self.y = y
        self.Neighboors = n

    def __getitem__(self,a):
        #print(a)
        return self.Bomb, self.x, self.y, self.Neighboors

    def add_Neigh(self, n):
        self.Neighboors.append(n)

    def add_Neigh_List(self, nodes):
        self.Neighboors + nodes

class Maze:
    def __init__(self, N=5):
        self.Map = []
        self.displayed = []
        self.create_MazeBomb(N)
        self.create_flip()
        self.stack_neigh()

    def __str__(self):
        return self.displayed

    def __getitem__(self, pos):
        x,y = pos
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

    def stack_neigh(self):
        x = 0
        l = self.N - 1
        for row in self.Map:
            y=0
            for node in row:
                for a in (-1,0,1):
                    for b in (-1,0,1):
                        if((a==0)&(b==0)):
                            pass
                        elif(((x+a)<0)|((x+a)>l)|((y+a)<0)|((y+a)>l)|((x+b)<0)|((x+b)>l)|((y+b)<0)|((y+b)>l)):
                            pass
                        else:
                            n = self.Map[x+a][y+b]
                            node.add_Neigh(n)
                y+=1
            x+=1

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

    #m.stack_neigh_debug()
    a = m[1, 0]
    print("hi")
    m.print_realMap()
    #m.revealCase(1,1)
    #while(1):
        #wait user move
        #m.print_Map()
        #reveal case
        #check if bomb
        #ifBomb
            #endgame
        #else
            #continue
