import pygame
from objective.chessboardLayout import Chessboard


def draw_board(board_size, swapSide=False):
    pygame.init()
    pygame.display.set_caption("Play the chess game")
    colors = [(255, 255, 255), (0, 255, 0)]  # Set up colors [white, green]

    n = board_size  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_len = surface_sz // n  # sq_sz is length of a square.
    print(sq_len)
    # surface_sz = n * sq_sz     # Adjust window to exactly fit n squares.
    x_offset_of_Board = 150
    y_offset_of_Board = 150
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 0, 0)
    surface.fill(colorOfTheSurface)
    chessboard = Chessboard(surface, x_offset_of_Board, y_offset_of_Board, sq_len)
    chessboard.insertFiguresIntoChessboard(chessboard.chessboardFields, n)
    while True:
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_len + x_offset_of_Board, row * sq_len + y_offset_of_Board, sq_len, sq_len)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        pygame.display.set_caption("game")
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos_of_click = ev.dict['pos']
            field = chessboard.getNameOfField((pos_of_click[0], pos_of_click[1]))
            print(field)

        chessboard.insertFiguresIntoChessboard(chessboard.chessboardFields, n)
        pygame.display.flip()  # displaying pygame window

    pygame.quit()


if __name__ == "__main__":
    draw_board(8)