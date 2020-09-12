import numpy as np
import random


def runProgram():
    size = int(input('Input size of the game board: '))
    gameBoard = makeGameBoard(size)
    userSymbol = input('Select your tic tac toe symbol: ')
    for i in range(0, size*size-1):
        print('Input coordinates of your move: ')
        xValue, yValue = [int(x) for x in input().split()]
        # # gameBoard[xValue][yValue] = userSymbol
        userMove(xValue, yValue, userSymbol, gameBoard)
        prettyPrintGameboard(gameBoard)
        computerMove(gameBoard)
        prettyPrintGameboard(gameBoard)


def makeGameBoard(size: int):
    gameBoard = ["-"] * size
    for i in range(0, size):
        gameBoard[i] = ["-"] * size
    return gameBoard


def userMove(xValue:int, yValue:int, userSymbol:str, gameBoard):  # niestety nadpisuje istniejace w tabeli symbole
    gameBoard[xValue][yValue] = userSymbol
    return gameBoard


def computerMove(gameBoard): # zrobiono tak ze nie nadpisuje juz istniejacych w tabeli symboli
    i = 0
    while i < 100:
        xValue = random.randint(0,len(gameBoard)-1)
        yValue = random.randint(0,len(gameBoard)-1)

        if gameBoard[xValue][yValue] == '-':
            gameBoard[xValue][yValue] = 'x'
            break
        else:
            i+=1

    return gameBoard


def checkWinning(gameboard):
    pass


def prettyPrintGameboard(gameBoard):
    print("---------------")
    for i in range(0, len(gameBoard)):
        print(gameBoard[i])
    print("---------------")




if __name__ == "__main__":
    runProgram()
