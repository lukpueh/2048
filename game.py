import random, os
import _Getch

HIGHEST = 0
EMPTY = ' '

def prettyPrint(grid):
    n = len(grid)

    print(chr(27) + "[2J")

    for row in range(n):

        line = ' | '.join([str(tile).center(len(str(HIGHEST)), ' ') for tile in grid[row]])

        lineSep =  '-' * len(line)
        print line, '\n', lineSep
    print '\n'

def createEmpty(n):
    return [[EMPTY for col in range(n)] for row in range(n)]

def flip(grid):
    n = len(grid)
    return [[grid[row][col] for col in range(n - 1, -1, -1)] for row in range(n)]

def transpose(grid):
    n = len(grid)
    return [[grid[col][row] for col in range(n)] for row in range(n)]

def moveLeft(grid):
    global HIGHEST
    n = len(grid)
    target = createEmpty(n)
    for row in range(n):
        targetIdx = 0
        for col in range(n):
            tile = grid[row][col]

            if tile == EMPTY:
                continue

            if target[row][targetIdx] == EMPTY:
                target[row][targetIdx] = tile
            else:
                if target[row][targetIdx] == tile:
                    target[row][targetIdx] = tile * 2

                    if HIGHEST < tile * 2:
                        HIGHEST = tile * 2
                else:
                    target[row][targetIdx + 1] = grid[row][col]
                targetIdx += 1
    return target 

def move(grid, direction):
    if direction == "left":
        grid = moveLeft(grid)
    elif direction == "right":
        grid = flip(moveLeft(flip(grid)))
    elif direction == "up":
        grid = transpose(moveLeft(transpose(grid)))
    elif direction == "down":
        grid = transpose(flip(moveLeft(flip(transpose(grid)))))

    return grid


def addTwo(grid):
    n = len(grid)
    emptyList = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == EMPTY:
                emptyList.append((row, col))

    length = len(emptyList)     
    if length < 1:
        return False

    coord = emptyList[random.randint(0, length - 1)]
    grid[coord[0]][coord[1]] = 2
    return grid


def main():
    grid = createEmpty(4)
    grid = addTwo(grid)
    grid = addTwo(grid)

    while True:
        os.system('cls')
        prettyPrint(grid)

        key = _Getch.getch()

        if key == 'w':
            grid = move(grid, "up")
        elif key == 's':
            grid = move(grid, "down")
        elif key == 'a':
            grid = move(grid, "left")
        elif key == 'd':
            grid = move(grid, "right")
        elif key == 'q':
            break
        else:
            continue

        grid = addTwo(grid)
        if not grid:
            print "So long, Sucker!"
            break

if __name__=='__main__':
    main()

