import pygame
import pygame_widgets as pw
from boardInitialisation import generateFieldNames, initFigures, insertFiguresIntoChessboard,\
    chessboardSquareNotation, getNameOfField


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
    white_position, black_position, figurePos = insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
    print(white_position)
    print(black_position)
    move = 0
    while True:
        return_to_menu.draw()
        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz + x_offset_of_Board, row * sq_sz + y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        # insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)

        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:

            if ev.button is 1:  # 1- left button of the mouse
                pos = pygame.mouse.get_pos()
                pos_of_click = ev.dict['pos']
                if pos_of_click[0] >=return_to_menu.getX() and pos_of_click[0] < return_to_menu.getX()+return_to_menu.width and pos_of_click[1] >=return_to_menu.getY() and pos_of_click[1] < return_to_menu.getY()+return_to_menu.height:
                    break
                elif pos_of_click[0] >= x_offset_of_Board and pos_of_click[0]< x_offset_of_Board+ surface_sz and pos_of_click[1] >= y_offset_of_Board and pos_of_click[1] < y_offset_of_Board + surface_sz:
                    print(pos_of_click)
                    field_name = getNameOfField(board_field_names, pos_of_click, x_offset_of_Board, y_offset_of_Board, sq_sz)
                    clickInFieldToMoveFigure(pos_of_click[0], pos_of_click[1], field_name, figurePos)

        if move == 0:
            insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
        else:
            newChessboardLayout(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
        pygame.display.flip()  # displaying pygame window


def clickInFieldToMoveFigure(x_pos, y_pos, boardFieldName, figuresPosition):
    print("Selected: " + boardFieldName)
    checkIfIsThereFigure(boardFieldName, figuresPosition)
    # sprawdzić czy w danym miejscu rzeczywiście jest figura
    pass


def checkIfIsThereFigure(boardFieldName, figuresPosition):
    try:
        print(figuresPosition[boardFieldName])
    except:
        print("None figure")


def moveFigure(typeOfFigure, newField, surface, chessboard, sq_size):
    # usunac figure ze starego pola, dodac figure na nowym polu
    # zanim wywołamy tą funkcje to trzeba sprawdzić czy nic tej figury nie przysłania i czy może dany ruch wykonać
    surface.blit(pygame.transform.scale(typeOfFigure, (50, 50)),
                 (chessboard[newField][1] + (sq_size / 2), chessboard[newField][0] + (sq_size / 2)))


def newChessboardLayout(whiteFigures, blackFigures, surface, chessboard, sq_size):
    w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = whiteFigures
    for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
        surface.blit(pygame.transform.scale(w_pawn, (50, 50)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
    figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
    for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
        surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))

    b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = blackFigures
    for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
        surface.blit(pygame.transform.scale(b_pawn, (50, 50)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
    figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
    for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
        surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))