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

    def get_Neigh(self):
        return self.Neighboors

    def add_Neigh(self, node):
        self.Neighboors.append(node)

    def add_Neigh_List(self, nodes):
        self.Neighboors + nodes

class Maze:
    def __init__(self):
        self.Map = []

    def create_MazeBomb(self,N):
        self.N=N
        for x in range(N):
            for y in range(N):
                row = []
                n = Node(x, y)
                row.append(n)

            self.Map.append(row)

    def flip_Maze(self):
        self.Map = [(0,0,0,0),
                    (0,0,0,0),
                    (0,0,0,0)]

    def print_Map(self):
        for i in range(self.N): print(self.Map[0:self.N])


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    m = Maze()
    m.create_MazeBomb(5)
    m.print_Map()

