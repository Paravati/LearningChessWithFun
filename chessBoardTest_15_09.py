# https://openbookproject.net/thinkcs/python/english3e/pygame.html
# https://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#eightqueensmainprog
import pygame
import numpy as np
import random


def startGame():
    pygame.init()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (200, 100, 220)
    surface.fill(colorOfTheSurface)
    isNewGame = True
    myFont = pygame.font.SysFont("Courier", 30, bold=True)
    while True:
        surface.fill(colorOfTheSurface)
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            isNewGame = False
            draw_board([6, 4, 2, 0, 5, 7, 1, 3])

        if isNewGame is False:
            text = myFont.render("You lost! Click to try again", True, (30, 30, 30), colorOfTheSurface)
            surface.blit(text, (0, 0))

        pygame.display.flip()  # displaying pygame window
    pygame.quit()
    # inp = input("Hello! This is chess learning module.\n Do you wanna play (click 1 if yes)? ")
    # if inp is '1':
    #     draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # else:
    #     print("OK, next time :) ")


def draw_board(the_board):
    pygame.init()
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
    colorOfTheSurface = (200, 100, 220)
    surface.fill(colorOfTheSurface)
    myFont = pygame.font.SysFont("Courier", 50, bold=True)
    mySmallFont = pygame.font.SysFont("Courier", 20, bold=True)

    fieldForUser = generateFieldForUser(board_field_names)  # initialization a first quest for user
    the_text = myFont.render(generateText(fieldForUser), True, (0, 30, 0), (255, 255, 255))
    surface.blit(the_text, (200, 80))
    chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, generateFieldNames(n))
    print(chessBoard)
    userPoints = 0
    while True:
        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz + x_offset_of_Board, row * sq_sz + y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard, sq_size=n)

        # Look for an event from keyboard, mouse, etc.
        newText = myFont.render("Where is: " + generateText(fieldForUser), True, (0, 30, 0), colorOfTheSurface)
        surface.blit(newText, (200, 80))

        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_of_click = ev.dict['pos']
            print(pos_of_click)
            field_name = getNameOfField(board_field_names, pos_of_click, x_offset_of_Board, y_offset_of_Board, sq_sz)
            if field_name == fieldForUser:
                the_text = mySmallFont.render(generateText("Passed: " + field_name), True, (0, 0, 0), colorOfTheSurface)
                userPoints += 1
                textWithPoints = mySmallFont.render("Points: " + str(userPoints), True, (0, 0, 0), colorOfTheSurface)
                surface.blit(textWithPoints, (645, 500))
                surface.blit(the_text, (645, 550))
                # surface.blit(the_text)
                fieldForUser = generateFieldForUser(board_field_names)
            else:
                the_text = mySmallFont.render(generateText("This is:" + field_name), True, (0, 0, 0), colorOfTheSurface)
                surface.blit(the_text, (645, 550))
                return 0

        pygame.display.flip()  # displaying pygame window
    pygame.quit()


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
    w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = whiteFigures
    for field in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
        surface.blit(pygame.transform.scale(w_pawn, (40, 40)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
    figures = [w_rook, w_horse, w_bishop, w_queen, w_king, w_bishop, w_horse, w_rook]
    for i, fields in enumerate(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
        surface.blit(pygame.transform.scale(figures[i], (40, 40)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))

    b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = blackFigures
    for field in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
        surface.blit(pygame.transform.scale(b_pawn, (40, 40)),
                     (chessboard[field][1] + (sq_size / 2), chessboard[field][0] + (sq_size / 2)))
    figures = [b_rook, b_horse, b_bishop, b_queen, b_king, b_bishop, b_horse, b_rook]
    for i, fields in enumerate(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']):
        surface.blit(pygame.transform.scale(figures[i], (40, 40)),
                     (chessboard[fields][1] + (sq_size / 2), chessboard[fields][0] + (sq_size / 2)))


def chessboardSquareNotation(n, sq_len, x_offset_of_Board, y_offset_of_Board, listWithFieldNames):
    chessBoard = {}
    for row in range(n):  # Draw each row of the board.
        for col in range(n):  # Run through cols drawing squares
            the_square = (col * sq_len + x_offset_of_Board, row * sq_len + y_offset_of_Board, sq_len, sq_len)
            dictTmp = {listWithFieldNames[row][col]: the_square}
            chessBoard.update(dictTmp)

    return chessBoard


def generateFieldForUser(listWithFieldNames):
    line = random.choice(listWithFieldNames)
    return random.choice(line)


def generateFieldNames(boardSize):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [8, 7, 6, 5, 4, 3, 2, 1]
    listWithFieldNames = np.ndarray(shape=(boardSize, boardSize), dtype='object')
    for rows in range(0, len(listWithFieldNames)):
        for col in range(0, len(listWithFieldNames)):
            listWithFieldNames[rows][col] = letters[rows] + str(numbers[col])
    return listWithFieldNames


def getNameOfField(listWithFieldNames, pos, offset_X, offset_Y, lenSquare):
    clickedField = ""
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


if __name__ == "__main__":
    startGame()
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])

    # draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
