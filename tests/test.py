import pytest

from utils import sumotori as sumo
from Game import *


def test_Node(n = Node(0, 0)):

    assert isinstance(n.__str__(), str)
    assert len(n.__getitem__()) == 4
    assert isinstance(n.isrevealed(), bool)


def test_Maze(env = Maze(10)):

    assert len(env.displayed) == (env.N * env.N)
    test_Node(env.__getitem__((0, 0)))


def test_Neighboor_Consitancy():
    env = Maze(3)
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            if (i % 2 == 0) & (j % 2 == 0):
                assert len(env.__getitem__((i, j)).Neighboors) == 3
            elif (i == 1) & (j == 1):
                assert len(env.__getitem__((i, j)).Neighboors) == 8
            else:
                assert len(env.__getitem__((i, j)).Neighboors) == 5

def test_Neighboor_exact():
    env = Maze(3)
    node1 = env.Map[0][0]
    node2 = env.Map[0][1]
    node3 = env.Map[0][2]
    node4 = env.Map[1][0]
    node5 = env.Map[1][1]
    node6 = env.Map[1][2]
    node7 = env.Map[2][0]
    node8 = env.Map[2][1]
    node9 = env.Map[2][2]

    assert node1.Neighboors == [node2, node4, node5]
    assert node2.Neighboors == [node1, node3, node4, node5, node6]
    assert node3.Neighboors == [node2, node5, node6]
    assert node4.Neighboors == [node1, node2, node5, node7, node8]
    assert node5.Neighboors == [node1, node2, node3, node4, node6, node7, node8, node9]
    assert node6.Neighboors == [node2, node3, node5, node8, node9]
    assert node7.Neighboors == [node4, node5, node8]
    assert node8.Neighboors == [node4, node5, node6, node7, node9]
    assert node9.Neighboors == [node5, node6, node8]


def test_integration():
    env = Maze(3)
    env.debugMap()
    env.update_dispMap()
    test_Maze(env)
    assert env.displayed == ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    env.revealCase(0,0)
    env.update_dispMap()
    assert env.displayed == ['1', '.', '.', '.', '.', '.', '.', '.', '.']
    env.revealCase(0,1)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '.', '.', '.', '.', '.', '.', '.']
    env.revealCase(0,2)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '.', '.', '.', '.', '.', '.']
    env.revealCase(1,0)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '1', '.', '.', '.', '.', '.']
    env.revealCase(1,2)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '1', '.', '1', '.', '.', '.']
    env.revealCase(2,0)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '1', '.', '1', '1', '.', '.']
    env.revealCase(2,1)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '1', '.', '1', '1', '1', '.']
    env.revealCase(2,2)
    env.update_dispMap()
    assert env.displayed == ['1', '1', '1', '1', '.', '1', '1', '1', '1']
