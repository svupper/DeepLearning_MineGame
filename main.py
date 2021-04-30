# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

class Node:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.Neighboors = []

    def get_Nodes(self):
        return self.

class Maze:
    def __init__(self):
        self.Map = []

    def create_MazeBomb(self,N):
        self.Map = []
        for i in range(N*N):
            self.Map.append(random.randint(0, 1))

    def flip_Maze(self):
        self.Map = [(0,0,0,0),
                (0,0,0,0),
                (0,0,0,0)]

    def print_Map(self):
        for i in self.Map: print(i)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    create_MazeBomb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
