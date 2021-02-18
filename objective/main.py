import pygame
from objective.chessboardCreator import Chessboard

def updatePosOfTheFigure(self, surface):   # for drag and drop event in the future :D
    if self.click:
        self.rect.center = pygame.mouse.get_pos()
    surface.blit(self.image, self.rect)


def coloringChessboard(surface, n, sq_len, x_offset, y_offset, pointedPiece, colors):
    for row in range(n):  # Draw each row of the board.
        c_indx = row % 2  # Change starting color on each row
        for col in range(n):  # Run through cols drawing squares
            the_square = (col * sq_len + x_offset, row * sq_len + y_offset, sq_len, sq_len)
            if pointedPiece is not None and the_square[0] == pointedPiece[1] and the_square[1]==pointedPiece[0]:
                surface.fill((100, 100, 100), the_square)
            else:
                surface.fill(colors[c_indx], the_square)
            c_indx = (c_indx + 1) % 2


def draw_board(board_size, swapSide=False):
    pygame.init()
    pygame.display.set_caption("Play the chess game")
    colors = [(255, 255, 255), (0, 255, 0)]  # Set up colors [white, green]
    n = board_size  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_len = surface_sz // n  # sq_sz is length of a square.
    # surface_sz = n * sq_sz     # Adjust window to exactly fit n squares.
    x_offset_of_Board = 150
    y_offset_of_Board = 150
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 0, 0)
    surface.fill(colorOfTheSurface)
    chessboard = Chessboard(surface, x_offset_of_Board, y_offset_of_Board, sq_len)
    checkedField1st = None
    checkedField2nd = None
    move = 0
    pointedField = None  # field which will be in different color when pointed by user
    coloringChessboard(surface, n, sq_len, x_offset_of_Board, y_offset_of_Board, pointedField, colors)
    chessboard.insertFiguresIntoChessboard(chessboard.chessboardFields, n)

    while True:
        pygame.display.set_caption("game")
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN and checkedField2nd is None:
            pos_of_click = ev.dict['pos']
            if x_offset_of_Board < pos_of_click[0] < surface.get_height():
                if y_offset_of_Board < pos_of_click[1] < surface.get_width():
                    checkedField1st = chessboard.getNameOfField((pos_of_click[0], pos_of_click[1]))
                    if chessboard.figurePos[checkedField1st] is not None:
                        if move % 2 == 0:
                            if chessboard.figurePos[checkedField1st][0] == 'w':
                                pointedField = chessboard.chessboardFields[checkedField1st]
                            else:
                                checkedField1st = None
                        else:
                            if chessboard.figurePos[checkedField1st][0] == 'b':
                                pointedField = chessboard.chessboardFields[checkedField1st]
                            else:
                                checkedField1st = None
        if ev.type == pygame.MOUSEBUTTONDOWN and checkedField1st is not None and chessboard.figurePos[checkedField1st] is not None:  # only if user clicked on field with figure then we can check field to move
            pos_of_click = ev.dict['pos']
            if x_offset_of_Board < pos_of_click[0] < surface.get_height():
                if y_offset_of_Board < pos_of_click[1] < surface.get_width():
                    checkedField2nd = chessboard.getNameOfField((pos_of_click[0], pos_of_click[1]))
                    if checkedField2nd != checkedField1st:  # move figure
                        isMoveHappen = chessboard.moveFigure(checkedField1st, checkedField2nd, chessboard.figurePos[checkedField1st])
                        if isMoveHappen:
                            move += 1
                        chessboard.insertFiguresIntoChessboardAfter1stMove(n)
                        checkedField1st = None
                        checkedField2nd = None
                        pointedField = None

        # chessboard.insertFiguresIntoChessboard(chessboard.chessboardFields, n)
        if move == 0:
            coloringChessboard(surface, n, sq_len, x_offset_of_Board, y_offset_of_Board, pointedField, colors)
            chessboard.insertFiguresIntoChessboard(chessboard.chessboardFields, n)
        else:
            coloringChessboard(surface, n, sq_len, x_offset_of_Board, y_offset_of_Board, pointedField, colors)
            chessboard.insertFiguresIntoChessboardAfter1stMove(n)

        pygame.display.flip()  # displaying pygame window

    pygame.quit()


if __name__ == "__main__":
    draw_board(8)
