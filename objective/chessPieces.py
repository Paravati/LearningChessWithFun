def pawnMoves(IsfirstMove, oldPos, color):
    possiblePos = []
    coef = 1 if color == "w" else -1
    move1 = int(oldPos[-1]) + coef * 1
    if IsfirstMove:  # Move 1 or 2 field
        possiblePos.append(oldPos[0] + str(move1))
        move2 = int(oldPos[-1]) + coef * 2
        possiblePos.append(oldPos[0] + str(move2))
    else:  # move only for one point
        possiblePos.append(oldPos[0] + str(move1))

    return possiblePos


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