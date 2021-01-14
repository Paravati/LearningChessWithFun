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


def bishopMoves(oldPos, allFigurePos, chessboard_fields):
    # todo:
    iterator = len(chessboard_fields[0])
    # print(chessboard_fields)
    possiblePos = []
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    print(oldPosCharacter)
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop

    for i in range(iterator):
        for j in range(iterator):
            if i ==oldPosNumber-1 and j==oldPosCharNumber:
                # print(oldPosNumber)
                # print(oldPosCharNumber)
                if i == iterator-1:  # only for upper position bishop i = 7
                    jTmp = j
                    iTmp = i
                    while jTmp-1 >= 0 and iTmp >= 1:
                        possiblePos.append(chessboard_fields[iterator - iTmp][jTmp-1])
                        print("FIRST -> 1." + str(possiblePos))
                        jTmp -=1
                        iTmp -=1
                    jTmp = j
                    iTmp = i
                    while jTmp+1 < iterator and iTmp >= 1:
                        possiblePos.append(chessboard_fields[iterator - iTmp][jTmp + 1])
                        print("FIRST -> 2.  " + str(possiblePos))
                        jTmp += 1
                        iTmp -= 1
                if iterator-(i+2) >= 0:
                    jTmp = j
                    iTmp = i
                    while jTmp+1<iterator and iterator-(iTmp+2)>=0:  # right upper diagonal
                        possiblePos.append(chessboard_fields[iterator-(iTmp+2)][jTmp+1])
                        print("SECOND -> 1. " + str(possiblePos))
                        jTmp += 1
                        iTmp += 1
                    jTmp = j
                    iTmp = i
                    while jTmp-1 >= 0 and iterator-(iTmp+2)>=0:  # left upper diagonal
                        possiblePos.append(chessboard_fields[iterator - (iTmp + 2)][jTmp - 1])
                        print("SECOND -> 2.  " + str(possiblePos))
                        jTmp -= 1
                        iTmp += 1
                if i!= iterator-1 and iterator-i >= 0 and i!=0:
                    jTmp = j
                    iTmp = i
                    while jTmp-1 >= 0 and iterator - iTmp < iterator:  # left lower dagonal
                        possiblePos.append(chessboard_fields[iterator - iTmp][jTmp - 1])
                        print("THIRD -> 1.  " + str(possiblePos))
                        jTmp -= 1
                        iTmp -= 1
                    jTmp = j
                    iTmp = i
                    while jTmp+1<iterator and iterator - iTmp >= 0:  # right lower diagonal
                        possiblePos.append(chessboard_fields[iterator - iTmp][jTmp + 1])
                        print("THIRD -> 2. " + str(possiblePos))
                        jTmp += 1
                        iTmp += 1


    print(possiblePos)
    return possiblePos


def kingMoves():
    pass
# ****** FULL DIAGONAL FOR KING -> MOVES only for one field
# for i in range(iterator):
#     for j in range(iterator):
#         if i == oldPosNumber - 1 and j == oldPosCharNumber:
#             print(oldPosNumber)
#             print(oldPosCharNumber)
#             if i == iterator - 1:
#                 print("first")
#                 if j - 1 >= 0:
#                     possiblePos.append(chessboard_fields[iterator - i][j - 1])
#                 if j + 1 < iterator:
#                     possiblePos.append(chessboard_fields[iterator - i][j + 1])
#             if iterator - (i + 2) >= 0:
#                 print("second")
#                 if j + 1 < iterator:
#                     possiblePos.append(chessboard_fields[iterator - (i + 2)][j + 1])
#                 if j - 1 >= 0:
#                     possiblePos.append(chessboard_fields[iterator - (i + 2)][j - 1])
#             if i != iterator - 1 and iterator - i >= 0 and i != 0:
#                 print("third")
#                 if j - 1 >= 0:
#                     possiblePos.append(chessboard_fields[iterator - i][j - 1])
#                 if j + 1 < iterator:
#                     possiblePos.append(chessboard_fields[iterator - i][j + 1])

def queenMoves():
    pass


def rookMoves(oldPos, allFigurePos, chessboard_fields):
    # todo: ograniczanie pozycji wiezy, bicie
    iterator = len(chessboard_fields[0])
    # print(chessboard_fields)
    possiblePos = []
    oldPosNumber = int(oldPos[-1])  # pointed i in lower loop
    oldPosCharacter = oldPos[0]
    # print(oldPosCharacter)
    oldPosCharNumber = FieldNumerical(oldPosCharacter, None)  # pointed j in lower loop

    for i in range(iterator):
        if i == oldPosNumber-1:  # minus 1 because array starts from index 0
            for j in range(iterator):
                possiblePos.append(chessboard_fields[iterator - i-1][j])  # vertical possible positions
        if i == oldPosCharNumber:
            for j in range(iterator):
                possiblePos.append(chessboard_fields[j][i])  # horizontal possible positions
    # print(possiblePos)
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