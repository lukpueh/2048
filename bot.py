import game as g
import time

def copy(grid):
    n = len(grid)
    return [[grid[row][col] for col in range(n)] for row in range(n)]

def hasMoved(gridOld, gridNew):
    n = len(gridOld)
    moved = False
    for row in range(n):
        if moved:
            break

        for col in range(n):
            if gridOld[row][col] != gridNew[row][col]:
                moved = True
                break
    return moved

def move(grid):
    moveList = ["up", "left", "right", "down"]
    gridNew = copy(grid)
    for direction in moveList:
        gridOld = copy(gridNew)
        gridNew = g.move(gridOld, direction)
        if hasMoved(gridOld, gridNew):
            break
    return gridNew


def main():

    try:
        grid = g.createEmpty(4)
        grid = g.addTwo(grid)
        grid = g.addTwo(grid)
        moveCnt = 0
        while grid != False:
            time.sleep(.2)
            g.prettyPrint(grid)                
            grid = move(grid)
            moveCnt += 1
            grid = g.addTwo(grid)

        #print "Score:", g.HIGHEST, "Moves:", moveCnt
        #print g.HIGHEST, moveCnt
    except KeyboardInterrupt:
        pass


if __name__=='__main__':
    main()