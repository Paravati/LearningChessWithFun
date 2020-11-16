import pygame
import pygame_widgets as pw
from boardInitialisation import generateFieldNames, initFigures, insertFiguresIntoChessboard,\
    chessboardSquareNotation


def play():
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    pass


def draw_board(the_board):
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
    board_field_names = generateFieldNames(n)
    blackFigures, whiteFigures = initFigures()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 0, 0)
    surface.fill(colorOfTheSurface)
    return_to_menu = pw.Button(
        surface, 10, 550, 130, 65, text='Back',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )

    chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, generateFieldNames(n))
    insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
    while True:
        # surface.blit(backgroundIMG, (0,0))
        return_to_menu.draw()
        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz + x_offset_of_Board, row * sq_sz + y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)

        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:

            if ev.button is 1:  # 1- left button of the mouse
                pos = pygame.mouse.get_pos()
                pos_of_click = ev.dict['pos']
                if pos_of_click[0] >=return_to_menu.getX() and pos_of_click[0] < return_to_menu.getX()+return_to_menu.width and pos_of_click[1] >=return_to_menu.getY() and pos_of_click[1] < return_to_menu.getY()+return_to_menu.height:
                    break

        insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
        pygame.display.flip()  # displaying pygame window