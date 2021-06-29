from Game import *

if __name__ == '__main__':
    debug = False
    Loose = False
    Win = False
    m = Maze()
    if debug:
        m.debugMap()

    while not Loose:

        print("reveler une case svp (x): ")
        x = int(input())
        assert (x<m.N) & (x+1>0)

        print("reveler une case svp (y): ")
        y = int(input())
        assert (y<m.N) & (y+1>0)


        if m.Map[x][y].isBomb():
            Loose = True
            print("Perdu !")
            m.print_Bombs()
            break

        #Il All revealed without bomb WIN

        m.revealCase(x, y)
        m.print_Map()

