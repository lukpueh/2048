import random, os

class Game():
    """Simple implementation of game 2048"""
    def __init__(self, n = 4, empty = ' '):
        self.n = n
        self.empty = empty
        self.score = 0
        self.max = 0
        self.lost = False

        # Create new empty
        self.grid = self.createEmptyGrid()
        for x in range(2):
            self.add()


    def prettyPrint(self):
        """Clear screen and pretty print grid"""
        print(chr(27) + "[2J")
        print "Max:", self.max, "Score:", self.score
        for row in range(self.n):
            line = ' | '.join([str(tile).center(len(str(self.max)), ' ') for tile in self.grid[row]])
            lineSep =  '-' * len(line)
            print line, '\n', lineSep
        print '\n'

    def createEmptyGrid(self):
        """Create empty grid"""
        return [[self.empty for col in range(self.n)] for row in range(self.n)]

    def flip(self):
        """Mirror grid vertically"""
        self.grid = [[self.grid[row][col] for col in range(self.n - 1, -1, -1)] for row in range(self.n)]

    def transpose(self):
        """Transpose grid"""
        self.grid = [[self.grid[col][row] for col in range(self.n)] for row in range(self.n)]

    def moveLeft(self):
        """Move all tiles in all lines leftwards. 
        Start left if two tiles have the same number add them.
        return bool wheter grid has changed (moved)"""

        target = self.createEmptyGrid()

        # Iterate over source grid
        for row in range(self.n):
            targetColIdx = 0
            for col in range(self.n):
                tile = self.grid[row][col]

                # New tile in source, no action
                if tile == self.empty:
                    continue

                # Just copy from source to target
                if target[row][targetColIdx] == self.empty:
                    target[row][targetColIdx] = tile
                else:
                    # Merge tiles
                    if target[row][targetColIdx] == tile:
                        mergedTile = tile * 2
                        target[row][targetColIdx] = mergedTile

                        # Update score
                        self.score += mergedTile

                        # Update Max value
                        if self.max < mergedTile:
                            self.max = mergedTile
                    # Increment targetColIdx and copy from source to target
                    else:
                        target[row][targetColIdx + 1] = tile
                    targetColIdx += 1

        moved = not self.grid == target
        self.grid = target
        return moved

    def move(self, direction):
        """Only moveLeft is implemented, therefor 
        flip and/or transpose Matrix if needed"""
        moved = False
        if direction == "left":
            moved = self.moveLeft()
        elif direction == "right":
            self.flip()
            moved = self.moveLeft()
            self.flip()
        elif direction == "up":
            self.transpose()
            moved = self.moveLeft()
            self.transpose()
        elif direction == "down":
            self.transpose()
            self.flip()
            moved = self.moveLeft()
            self.flip()
            self.transpose()

        return moved

    def add(self):
        """Randomly add tile, currently only number 2"""
        # Create a list of all empty tiles in grid
        emptyTiles = []
        for row in range(self.n):
            for col in range(self.n):
                if self.grid[row][col] == self.empty:
                    emptyTiles.append((row, col))

        length = len(emptyTiles)     

        # Else randomly add a tile
        coord = emptyTiles[random.randint(0, length - 1)]
        self.grid[coord[0]][coord[1]] = 2

    def canMove(self):
        """Check if we can move"""
        for row in range(self.n):
            for col in range(self.n):
                # If there is an empty tile we can move
                if self.grid[row][col] == self.empty:
                    return True

                #If there are two same numbers next to each other we can move
                if col < self.n - 1 and \
                    self.grid[row][col] == self.grid[row][col + 1]:
                    return True
                if row < self.n -1 and \
                    self.grid[row][col] == self.grid[row + 1][col]:
                    return True
        return False



    def turn(self, direction):
        """ Move and add, if move was possible"""
        moved = False
        if (self.canMove()):
            moved = self.move(direction)
            if(moved):
                self.add()
        else:
            self.lost = True
        return moved


def main():
    import _Getch

    game = Game()

    while not game.lost:
        os.system('cls')
        game.prettyPrint()

        key = _Getch.getch()

        if key == 'w':
            game.turn("up")
        elif key == 's':
            game.turn("down")
        elif key == 'a':
            game.turn("left")
        elif key == 'd':
            game.turn("right")
        elif key == 'q':
            break
        else:
            continue

    print "So long sucker!"

if __name__=='__main__':
    main()

