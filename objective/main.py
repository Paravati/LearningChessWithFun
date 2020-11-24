import pygame
from objective.chessboardLayout import Chessboard


def draw_board(the_board, swapSide, randomSwap):
    pygame.init()
    pygame.display.set_caption("Play the chess game")
    colors = [(255, 255, 255), (0, 255, 0)]  # Set up colors [white, green]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    print(sq_sz)
    # surface_sz = n * sq_sz     # Adjust window to exactly fit n squares.
    x_offset_of_Board = 150
    y_offset_of_Board = 150
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 0, 0)
    surface.fill(colorOfTheSurface)
    chessboard = Chessboard()
    chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board,
                                          generateFieldNames(n, swapSide))
    the_text = mySmallFont.render(generateText(""), True, (255, 255, 255), colorOfTheSurface)
    textWithPoints = mySmallFont.render(generateText(""), True, (255, 255, 255), colorOfTheSurface)
    userPoints = 0
    insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
    while True:
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz + x_offset_of_Board, row * sq_sz + y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        pygame.display.set_caption("menu")
        surface.fill(colorOfTheSurface)
        surface.blit(pygame.transform.scale(backgroundIMG, (800, 650)), (0, 0))
        ev = pygame.event.poll()
        # surface.blit(pygame.transform.scale(titleIMG, (600,200)),(surface.get_height()/6, 50))
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos_of_click = ev.dict['pos']
            print(pos_of_click)
        pygame.display.flip()  # displaying pygame window

    pygame.quit()
