from enum import auto


def FieldNumerical(letter, value):
    listWithLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if letter is not None:
        for i in range(len(listWithLetters)):
            if listWithLetters[i] == letter:
                return i
    else:
        return listWithLetters[value] if (value >=0 and value<=7) else None

def defineDirectionsOfTheChessBoard(listWithFieldNames):
    diagonal = []
    horizontal = []
    vertical = []

def PawnbeatingMoves(oldPos, allFigurePosition, coef):
    letterNum = FieldNumerical(oldPos[0], None)
    beatingMovesLetters = [letterNum + 1, letterNum - 1]  # only letters
    beatingMoves = []
    for i in range(len(beatingMovesLetters)):
        if beatingMovesLetters[i] >=0 and beatingMovesLetters[i] < 8:
            move = int(oldPos[-1]) + coef*1
            fieldName = FieldNumerical(None, beatingMovesLetters[i]) + str(move)
            # print("Heello: " + fieldName)
            if allFigurePosition[fieldName] is not None:  # if figure on the pointed position exists
                beatingMoves.append(fieldName)

    return beatingMoves


def pawnMoves(IsfirstMove, oldPos, color, allFigurePos):
    possiblePos = []
    coef = 1 if color == "w" else -1
    move1 = int(oldPos[-1]) + coef * 1
    if IsfirstMove:  # Move 1 or 2 field
        if allFigurePos[oldPos[0] + str(move1)] is None:
            possiblePos.append(oldPos[0] + str(move1))
        move2 = int(oldPos[-1]) + coef * 2
        if allFigurePos[oldPos[0] + str(move2)] is None:
            possiblePos.append(oldPos[0] + str(move2))
    else:  # move only for one point
        if allFigurePos[oldPos[0] + str(move1)] is None:
            possiblePos.append(oldPos[0] + str(move1))
    possiblePos.extend(PawnbeatingMoves(oldPos, allFigurePos, coef))

    return possiblePos


def bishopMoves(oldPos, color, chessboard_fields):
    for i in range(len(chessboard_fields)):
        for j in range(len(chessboard_fields[i])):
            if chessboard_fields[i][j] == oldPos:
                # trzeba wczesniej okreslic diagonale calej szachownicy zeby szybciej odniesc sie do tego
                pass

    pass


def kingMoves():
    pass


def queenMoves():
    pass


def rookMoves(oldPos, allFigurePos, chessboard_fields):
    # todo: ograniczanie pozycji wiezy, bicie, poprawki wyznaczania pozycji dla koloru czarnego
    # todo: bo dla bialego dziala
    possiblePos = []
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    print(oldPosCharacter)
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop
    for i in range(len(chessboard_fields)):
        if i == oldPosNumber-1:  # minus 1 because array starts from index 0
            for j in range(len(chessboard_fields)):
                # if allFigurePos[chessboard_fields[i][j+1]] is not None:
                #     break  # rook cannot moves through another figures
                possiblePos.append(chessboard_fields[i][j])  # vertical possible positions
        if i == oldPosCharNumber:
            for j in range(len(chessboard_fields)):
                # if allFigurePos[chessboard_fields[j+1][i]] is not None:
                #     break  # rook cannot moves through another figures
                possiblePos.append(chessboard_fields[j][i])  # horizontal possible positions

    print(possiblePos)
    return possiblePos


def knightMoves():
    pass


class Pawn():
    def __init__(self, color):
        self.firstMove = 2
        self.move = 1
        self.color = color
        self.img = 'C:/Users/Admin/PycharmProjects/TicTacToePython/figures/b_pawn.png'

    def loadImageObject(self, color):
        pass


class ChessPiece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position