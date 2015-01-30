import game as g
from random import shuffle
import time

def crazyBot(game):
    moveList = ["up", "left", "right", "down"]
    shuffle(moveList)
    for direction in moveList:
        if game.turn(direction):
            break

def simpleBot(game):
    moveList = ["up", "left", "right", "down"]
    for direction in moveList:
        if game.turn(direction):
            break

def main():

    try:
        print "max;score;movecnt;grid"
        for x in range(10000):
            game = g.Game()
            moveCnt = 0
            while not game.lost:
                #time.sleep(.1)
                crazyBot(game)
                #game.prettyPrint()                
                moveCnt += 1
            #time.sleep(.1)
            print game.max, ";", game.score, ";", moveCnt, ";", game.grid
    except KeyboardInterrupt:
        pass


if __name__=='__main__':
    main()