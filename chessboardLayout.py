import pygame


class Chessboard:
    def __init__(self, fields, whiteFigures, blackFigures, surface, x_offset, y_offset):
        self.fields = fields
        self.whiteFigures = whiteFigures
        self.blackFigures = blackFigures
        self.surface = surface
        self.figurePos = {}
        self.n = 8  # board 8x8
        self.x_offset = x_offset  # x_offset_of_Board
        self.y_offset = y_offset  # y_offset_of_Board

    def insertFiguresIntoChessboard(self, chessboard, sq_size):
        whiteFigurePosition = {}
        blackFigurePosition = {}
        w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = self.whiteFigures
        for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
            self.surface.blit(pygame.transform.scale(w_pawn, (50, 50)),
                         (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
            dictTmp = {field: 'w_pawn'}
            whiteFigurePosition.update(dictTmp)

        figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
        w_figureNames = ["w_rook", "w_horse", "w_bishop", "w_queen", "w_king", "w_bishop", "w_horse", "w_rook"]
        for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
            self.surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                         (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
            dictTmp = {fields: w_figureNames[i]}
            whiteFigurePosition.update(dictTmp)

            self.figurePos.update(whiteFigurePosition)

            b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = self.blackFigures
            b_figureNames = ["b_rook", "b_horse", "b_bishop", "b_queen", "b_king", "b_bishop", "b_horse", "b_rook"]
            for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
                self.surface.blit(pygame.transform.scale(b_pawn, (50, 50)),
                             (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
                dictTmp = {field: 'b_pawn'}
                blackFigurePosition.update(dictTmp)

            figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
            for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
                self.surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                             (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
                dictTmp = {fields: b_figureNames[i]}
                blackFigurePosition.update(dictTmp)

            self.figurePos.update(blackFigurePosition)

            return whiteFigurePosition, blackFigurePosition

    def chessboardSquareNotation(self, n, sq_len, listWithFieldNames, swap=False):
        chessBoard = {}
        if swap is True:
            for row in range(self.n):  # Draw each row of the board.
                for col in range(self.n):  # Run through cols drawing squares
                    the_square = (col * sq_len + self.x_offset, row * sq_len + self.y_offset, sq_len, sq_len)
                    dictTmp = {listWithFieldNames[n - row - 1][n - col - 1]: the_square}
                    chessBoard.update(dictTmp)
        else:
            for row in range(self.n):  # Draw each row of the board.
                for col in range(self.n):  # Run through cols drawing squares
                    the_square = (col * sq_len + self.x_offset, row * sq_len + self.y_offset, sq_len, sq_len)
                    dictTmp = {listWithFieldNames[row][col]: the_square}
                    chessBoard.update(dictTmp)

        return chessBoard