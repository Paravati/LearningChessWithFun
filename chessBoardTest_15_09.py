# https://openbookproject.net/thinkcs/python/english3e/pygame.html
# https://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#eightqueensmainprog
import pygame
import numpy as np
import sys
import random


def draw_board(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255,255,255), (0,255,0)]    # Set up colors [white, green]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    print(sq_sz)
    # surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
    x_offset_of_Board = 150
    y_offset_of_Board = 150
    board_field_names = generateFieldNames(n)
    blackFigures, whiteFigures = initFigures()
    surface = pygame.display.set_mode((800, 650))
    surface.fill((45, 60, 80))
    myFont = pygame.font.SysFont("Courier", 50, bold=True)

    fieldForUser = generateFieldForUser(board_field_names)  # initialization a first quest for user
    the_text = myFont.render(generateText(fieldForUser), True, (0, 30, 0), (255, 255, 255))
    textRect1 = the_text.get_rect()
    surface.blit(the_text, textRect1)
    chessBoard = chessboardSquareNotation(n, sq_sz, x_offset_of_Board, y_offset_of_Board, generateFieldNames(n))
    print(chessBoard)
    print(surface)
    while True:
        # surface = insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard)
        # Look for an event from keyboard, mouse, etc.
        newText = myFont.render(generateText(fieldForUser), True, (0, 30, 0), (255, 255, 255))
        surface.blit(newText, textRect1)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_of_click = ev.dict['pos']
            print(pos_of_click)
            field_name = getNameOfField(board_field_names, pos_of_click, x_offset_of_Board, y_offset_of_Board, sq_sz)
            if field_name == fieldForUser:
                the_text = myFont.render(generateText("You passed! " + field_name), True, (0, 30, 0), (255,255,255))
                textRect = the_text.get_rect()
                print(textRect)
                textRect.center = (800 // 2,  100)
                surface.blit(the_text, textRect)
                fieldForUser = generateFieldForUser(board_field_names)

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Change starting color on each row
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz+x_offset_of_Board, row*sq_sz+y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2
        
        insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessBoard)
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


def insertFiguresIntoChessboard(whiteFigures, blackFigures, surface, chessboard):
    w_pawn, w_horse, w_bishop, w_rook, w_queen, w_king = whiteFigures
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['a2'][1], chessboard['a2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['b2'][1], chessboard['b2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['c2'][1], chessboard['c2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['d2'][1], chessboard['d2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['e2'][1], chessboard['e2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['f2'][1], chessboard['f2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['g2'][1], chessboard['g2'][0]))
    surface.blit(pygame.transform.scale(w_pawn, (40, 40)), (chessboard['h2'][1], chessboard['h2'][0]))

    b_pawn, b_horse, b_bishop, b_rook, b_queen, b_king = blackFigures
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['a7'][1], chessboard['a7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['b7'][1], chessboard['b7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['c7'][1], chessboard['c7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['d7'][1], chessboard['d7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['e7'][1], chessboard['e7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['f7'][1], chessboard['f7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['g7'][1], chessboard['g7'][0]))
    surface.blit(pygame.transform.scale(b_pawn, (40, 40)), (chessboard['h7'][1], chessboard['h7'][0]))


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
    for i in range(0,len(listWithFieldNames)):
        for j in range(0, len(listWithFieldNames)):
            if offset_X + lenSquare*i < pos[0] < offset_X+lenSquare*(i + 1) and pos[1] >offset_Y+lenSquare*j and pos[1] <offset_Y+lenSquare*(j + 1):
                clickedField = listWithFieldNames[i][j]
                print(listWithFieldNames[i][j])
    return clickedField


def generateText(inp):
    if inp is not None:
        return inp
    return "Hello world!!"


if __name__ == "__main__":
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])


    # draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

