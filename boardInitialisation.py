import pygame
import numpy as np
import pygame_widgets as pw
import random


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
    board_field_names = generateFieldNames(n, swapSide)
    blackFigures, whiteFigures = initFigures()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 0, 0)
    surface.fill(colorOfTheSurface)
    myFont = pygame.font.SysFont("Courier", 50, bold=True)
    mySmallFont = pygame.font.SysFont("Courier", 20, bold=True)
    return_to_menu = pw.Button(
        surface, 10, 550, 130, 65, text='Back',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )

    fieldForUser = generateFieldForUser(board_field_names)  # initialization a first quest for user
    chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, generateFieldNames(n,swapSide))
    the_text = mySmallFont.render(generateText(""), True, (255, 255, 255), colorOfTheSurface)
    textWithPoints = mySmallFont.render(generateText(""), True, (255, 255, 255), colorOfTheSurface)
    userPoints = 0
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

        newText = myFont.render("Where is: " + generateText(fieldForUser), True, (255, 255, 255), colorOfTheSurface)
        surface.blit(newText, (200, 80))

        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:

            if ev.button is 1:  # 1- left button of the mouse
                pos = pygame.mouse.get_pos()
                pos_of_click = ev.dict['pos']
                if pos_of_click[0] >=return_to_menu.getX() and pos_of_click[0] < return_to_menu.getX()+return_to_menu.width and pos_of_click[1] >=return_to_menu.getY() and pos_of_click[1] < return_to_menu.getY()+return_to_menu.height:
                    return userPoints
                if pos_of_click[0] >= x_offset_of_Board and pos_of_click[0]< x_offset_of_Board+ surface_sz and pos_of_click[1] >= y_offset_of_Board and pos_of_click[1] < y_offset_of_Board + surface_sz:
                    print(pos_of_click)
                    field_name = getNameOfField(board_field_names, pos_of_click, x_offset_of_Board, y_offset_of_Board, sq_sz)
                    if field_name == fieldForUser:
                        the_text = mySmallFont.render(generateText("Passed: " + field_name), True, (255, 255, 255), colorOfTheSurface)
                        userPoints += 1
                        textWithPoints = mySmallFont.render(generateText("Points: " + str(userPoints)), True, (255, 255, 255), colorOfTheSurface)
                        if randomSwap is False:
                            print(swapSide)
                            board_field_names = generateFieldNames(n, swapSide)
                            chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, board_field_names)
                            fieldForUser = generateFieldForUser(board_field_names)
                        else:
                            board_field_names = generateFieldNames(n, bool(random.randint(0,1)))
                            chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, board_field_names)
                            fieldForUser = generateFieldForUser(board_field_names)
                    else:
                        the_text = mySmallFont.render(generateText("This is:" + field_name), True, (255, 255, 255), colorOfTheSurface)
                        surface.blit(the_text, (645, 550))
                        return userPoints

        insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)
        surface.blit(textWithPoints, (645, 500))
        surface.blit(the_text, (645, 550))
        pygame.display.flip()  # displaying pygame window


def initFigures():
    b_bishop = pygame.image.load("figures/b_bishop.png")
    b_horse = pygame.image.load("figures/b_horse.png")
    b_king = pygame.image.load("figures/b_king.png")
    b_queen = pygame.image.load("figures/b_queen.png")
    b_pawn = pygame.image.load("figures/b_pawn.png")
    b_rook = pygame.image.load("figures/b_rook.png")
    w_bishop = pygame.image.load("figures/w_bishop.png")
    w_horse = pygame.image.load("figures/w_horse.png")
    w_king = pygame.image.load("figures/w_king.png")
    w_queen = pygame.image.load("figures/w_queen.png")
    w_pawn = pygame.image.load("figures/w_pawn.png")
    w_rook = pygame.image.load("figures/w_rook.png")
    return [b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king], [w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king]


def insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessboard, sq_size):
    whiteFigurePosition = {}
    blackFigurePosition = {}
    figurePosition = {}
    w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = whiteFigures
    for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
        surface.blit(pygame.transform.scale(w_pawn, (50, 50)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
        dictTmp = {field: 'w_pawn'}
        whiteFigurePosition.update(dictTmp)


    figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
    w_figureNames = ["w_rook", "w_horse", "w_bishop", "w_queen", "w_king", "w_bishop", "w_horse", "w_rook"]
    for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
        surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
        dictTmp = {fields: w_figureNames[i]}
        whiteFigurePosition.update(dictTmp)

    figurePosition.update(whiteFigurePosition)

    b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = blackFigures
    b_figureNames = ["b_rook", "b_horse", "b_bishop", "b_queen", "b_king", "b_bishop", "b_horse", "b_rook"]
    for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
        surface.blit(pygame.transform.scale(b_pawn, (50, 50)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
        dictTmp = {field: 'b_pawn'}
        blackFigurePosition.update(dictTmp)

    figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
    for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
        surface.blit(pygame.transform.scale(figures[i], (50, 50)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))
        dictTmp = {fields: b_figureNames[i]}
        blackFigurePosition.update(dictTmp)

    figurePosition.update(blackFigurePosition)

    return whiteFigurePosition, blackFigurePosition, figurePosition


def chessboardSquareNotation(n, sq_len, x_offset_of_Board, y_offset_of_Board, listWithFieldNames, swap=False):
    chessBoard = {}
    if swap is True:
        for row in range(n):  # Draw each row of the board.
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_len + x_offset_of_Board, row * sq_len + y_offset_of_Board, sq_len, sq_len)
                dictTmp = {listWithFieldNames[n-row-1][n-col-1]: the_square}
                chessBoard.update(dictTmp)
    else:
        for row in range(n):  # Draw each row of the board.
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_len + x_offset_of_Board, row * sq_len + y_offset_of_Board, sq_len, sq_len)
                dictTmp = {listWithFieldNames[row][col]: the_square}
                chessBoard.update(dictTmp)

    return chessBoard


def generateFieldForUser(listWithFieldNames):
    line = random.choice(listWithFieldNames)
    return random.choice(line)


def generateFieldNames(boardSize, swap=False):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [8, 7, 6, 5, 4, 3, 2, 1]
    if swap is True:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    listWithFieldNames = np.ndarray(shape=(boardSize, boardSize), dtype='object')
    for rows in range(0, len(listWithFieldNames)):
        for col in range(0, len(listWithFieldNames)):
            listWithFieldNames[rows][col] = letters[rows] + str(numbers[col])
    return listWithFieldNames


def getNameOfField(listWithFieldNames, pos, offset_X, offset_Y, lenSquare, swap=False):
    clickedField = ""
    if swap is True:
        for i in range(0, len(listWithFieldNames)):
            for j in range(0, len(listWithFieldNames)):
                if offset_X + lenSquare * i < pos[0] < offset_X + lenSquare * (i + 1) and pos[1] > offset_Y + lenSquare * j and pos[1] < offset_Y + lenSquare * (j + 1):
                    clickedField = listWithFieldNames[i][j]
                    print(listWithFieldNames[i][j])
    else:
        for i in range(0, len(listWithFieldNames)):
            for j in range(0, len(listWithFieldNames)):
                if offset_X + lenSquare * i < pos[0] < offset_X + lenSquare * (i + 1) and pos[1] > offset_Y + lenSquare * j and pos[1] < offset_Y + lenSquare * (j + 1):
                    clickedField = listWithFieldNames[i][j]
                    print(listWithFieldNames[i][j])
    return clickedField


def generateText(inp):
    if inp is not None:
        return inp
    return "Hello world!!"

if __name__=="__main__":
    fieldNames = generateFieldNames(8, False)
    print(fieldNames)
    fieldNames = generateFieldNames(8, True)
    print(fieldNames)