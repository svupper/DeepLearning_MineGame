from Game import *

if __name__ == '__main__':
    debug = False
    Loose = False
    Win = False
    env = Maze(10)

    while not Loose:
        env.print_Map()

        print("reveler une case svp (x): ")
        x = int(input())
        assert (x<env.N) & (x+1>0)

        print("reveler une case svp (y): ")
        y = int(input())
        assert (y<env.N) & (y+1>0)


        if env.Map[x][y].isBomb():
            Loose = True
            print("Perdu !")
            env.print_Bombs()
            break

        #Il All revealed without bomb WIN

        env.revealCase(x, y)
        env.print_Map()

