import pygame
import numpy as np
from figures import *
from objective.chessPieces import pawnMoves, queenMoves, kingMoves, knightMoves, rookMoves, bishopMoves
# todo: coloring field which user clicked,


class Chessboard:
    def __init__(self, surface, x_offset, y_offset, square_length):
        self.blackFigures, self.whiteFigures = self.initFigures()
        self.surface = surface
        self.n = 8  # board 8x8
        self.x_offset = x_offset  # x_offset_of_Board
        self.y_offset = y_offset  # y_offset_of_Board
        self.square_length = square_length
        self.fields = self.generateFieldNames()  # 2d list with all chessboard fields
        self.figurePos = self.startingDictionaryPosition()
        self.chessboardFields = self.chessboardSquareNotation(self.n,self.square_length, self.fields)

    def startingDictionaryPosition(self):
        figureDictPos = {}
        for i in range(0, 8):
            for j in range(0, 8):
                dictTmp = {self.fields[i][j]: None}
                figureDictPos.update(dictTmp)
        return figureDictPos

    def generateFieldNames(self, swap=False):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = [8, 7, 6, 5, 4, 3, 2, 1]
        if swap is True:
            letters = ["h", "g", "f", "e", "d", "c", "b", "a"]
            numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        listWithFieldNames = np.ndarray(shape=(8, 8), dtype='object')
        for rows in range(0, len(listWithFieldNames)):
            for col in range(0, len(listWithFieldNames)):
                listWithFieldNames[rows][col] = letters[col] + str(numbers[rows])
        return listWithFieldNames

    def insertFiguresIntoChessboard(self, chessboard, sq_size):
        whiteFigurePosition = {}
        blackFigurePosition = {}
        w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = self.whiteFigures
        figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
        w_figureNames = ["w_rook", "w_horse", "w_bishop", "w_queen", "w_king", "w_bishop", "w_horse", "w_rook"]
        for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
            self.surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                              (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
            dictTmp = {fields: w_figureNames[i]}
            whiteFigurePosition.update(dictTmp)

        for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
            self.surface.blit(pygame.transform.scale(w_pawn, (50, 50)), (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
            dictTmp = {field: 'w_pawn'}
            whiteFigurePosition.update(dictTmp)

        self.figurePos.update(whiteFigurePosition)

        b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = self.blackFigures
        b_figureNames = ["b_rook", "b_horse", "b_bishop", "b_queen", "b_king", "b_bishop", "b_horse", "b_rook"]
        for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
            self.surface.blit(pygame.transform.scale(b_pawn, (50, 50)), (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
            dictTmp = {field: 'b_pawn'}
            blackFigurePosition.update(dictTmp)

        figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
        for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
            self.surface.blit(pygame.transform.scale(figures[i], (50, 50)), (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
            dictTmp = {fields: b_figureNames[i]}
            blackFigurePosition.update(dictTmp)

        self.figurePos.update(blackFigurePosition)
        sorted(self.figurePos)

        return whiteFigurePosition, blackFigurePosition

    def insertFiguresIntoChessboardAfter1stMove(self, sq_size):
        path = 'C:/Users/Admin/PycharmProjects/TicTacToePython/figures/'
        for field in list(self.figurePos.keys()):
            if self.figurePos[field] is not None:
                self.surface.blit(pygame.transform.scale(pygame.image.load(path+self.figurePos[field]+".png"), (50, 50)), (self.chessboardFields[field][1] + (sq_size / 2), self.chessboardFields[field][0] + (sq_size / 2)))

    def moveFigure(self, oldPos, newPos, figureName):
        if self.figurePos[oldPos] is not None:
            canFigureMoveHere = self.checkPositionToMove(oldPos, newPos, figureName)  # moves which can be done by pointed figure
            if canFigureMoveHere:
                if self.figurePos[newPos] is None:  # if there is no figure at pointed new position
                    self.figurePos[newPos] = figureName
                    self.figurePos[oldPos] = None
                else:  # if there is figure in the new pointed position beating figure happening
                    print("beating figure")
                    self.figurePos[newPos] = figureName
                    self.figurePos[oldPos] = None
                return True
            else:  # if figure couldnt move
                return False

    def checkPositionToMove(self, oldPos, newPos, figure):
        """checking if pointed figure can move to pointed position
            returning: boolean value - True if figure can move to newPos and False if not;
            list with possible moves done by pointed figure"""
        figureColor = figure.split("_")[0]
        figureName = figure.split("_")[1]
        if figureName == "pawn":  # todo: dodać bicie na ukos wrogiej figury
            ifFirstMove = self.checkIfIsItFirstMove(oldPos)  # checking if it is first move of the pointed pawn
            possiblePos = pawnMoves(ifFirstMove, oldPos, figureColor, self.figurePos)
        elif figureName == 'bishop':
            possiblePos = bishopMoves(oldPos, figureColor, self.figurePos, self.fields)
        elif figureName == 'rook':
            possiblePos = rookMoves(oldPos, self.figurePos, self.fields)
        elif figureName == 'queen':
            possiblePos = queenMoves(oldPos, self.figurePos, self.fields)
        elif figureName == 'king':
            possiblePos = kingMoves(oldPos, figureColor, self.figurePos, self.fields)
        else:  # figureName is knight
            possiblePos = knightMoves(oldPos, figureColor, self.figurePos, self.fields)
            print("The hardest part here to point possible moves")

        if newPos in possiblePos:
            return True
        else:
            return False

    def checkIfIsItFirstMove(self, pos):
        listWithFirstMove = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
        if pos in listWithFirstMove:
            return True
        return False

    def chessboardSquareNotation(self, n, sq_len, listWithFieldNames):
        chessBoard = {}

        for col in range(self.n):  # Draw each row of the board.
            for row in range(self.n):  # Run through cols drawing squares
                the_square = (row * sq_len + self.x_offset, col * sq_len + self.y_offset, sq_len, sq_len)
                dictTmp = {listWithFieldNames[row][col]: the_square}
                chessBoard.update(dictTmp)

        return chessBoard

    def getNameOfField(self, pos):
        clickedField = ""
        for i in range(0, len(self.fields)):
            for j in range(0, len(self.fields)):
                if self.x_offset + self.square_length  * j < pos[0] < self.x_offset + self.square_length  * (j + 1) and pos[1] > self.y_offset + self.square_length  * i and pos[1] < self.y_offset + self.square_length  * (i + 1):
                    clickedField = self.fields[i][j]

        return clickedField


    def initFigures(self):
        path = 'C:/Users/Admin/PycharmProjects/TicTacToePython/'
        b_bishop = pygame.image.load(path+"figures/b_bishop.png")
        b_horse = pygame.image.load(path+"figures/b_horse.png")
        b_king = pygame.image.load(path+"figures/b_king.png")
        b_queen = pygame.image.load(path+"figures/b_queen.png")
        b_pawn = pygame.image.load(path+"figures/b_pawn.png")
        b_rook = pygame.image.load(path+"figures/b_rook.png")
        w_bishop = pygame.image.load(path+"figures/w_bishop.png")
        w_horse = pygame.image.load(path+"figures/w_horse.png")
        w_king = pygame.image.load(path+"figures/w_king.png")
        w_queen = pygame.image.load(path+"figures/w_queen.png")
        w_pawn = pygame.image.load(path+"figures/w_pawn.png")
        w_rook = pygame.image.load(path+"figures/w_rook.png")
        return [b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king], [w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king]


class ChessPiece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
