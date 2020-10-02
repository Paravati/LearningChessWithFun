# https://openbookproject.net/thinkcs/python/english3e/pygame.html
# https://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#eightqueensmainprog
import pygame
import numpy as np


def draw_board(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255,255,255), (0,0,0)]    # Set up colors [white, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    print(sq_sz)
    # surface_sz = n * sq_sz     # Adjust to exactly fit n squares.
    x_offset_of_Board = 150
    y_offset_of_Board = 150
    board_field_names = generateFieldNames(n)

    ball = pygame.image.load("bishop_white.png")
    ball = pygame.transform.scale(ball, (30, 30))
    ball_offset = (sq_sz - ball.get_width()) // 2
    # Create the surface of (width, height), and its window.
    # surface = pygame.display.set_mode((surface_sz, surface_sz))
    surface = pygame.display.set_mode((800, 650))
    surface.fill((45, 60, 80))
    myFont = pygame.font.SysFont("Courier", 50, bold=True)
    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_of_click = ev.dict['pos']
            print(pos_of_click)
            field_name = getNameOfField(board_field_names, pos_of_click, x_offset_of_Board, y_offset_of_Board, sq_sz)
            the_text = myFont.render(generateText("You passed! " + field_name), True, (0, 30, 0), (255,255,255))
            textRect = the_text.get_rect()
            textRect.center = (800 // 2,  100)
            surface.blit(the_text, textRect)
        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Change starting color on each row
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz+x_offset_of_Board, row*sq_sz+y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                surface.blit(ball, ((col * sq_sz + 150+ball_offset), row * sq_sz + 150+ ball_offset))
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        pygame.display.flip()  # displaying pygame window
    pygame.quit()


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

