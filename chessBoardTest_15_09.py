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

    ball = pygame.image.load("bishop_white.png")
    ball = pygame.transform.scale(ball, (30, 30))
    ball_offset = (sq_sz - ball.get_width()) // 2
    # Create the surface of (width, height), and its window.
    # surface = pygame.display.set_mode((surface_sz, surface_sz))
    surface = pygame.display.set_mode((800, 650))
    surface.fill((45, 60, 70))
    myFont = pygame.font.SysFont("Courier", 50,bold=True)
    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            the_text = myFont.render(generateText("You passed! " + str(pos)), True, (0, 30, 0), (255,255,255))
            textRect = the_text.get_rect()
            textRect.center = (800 // 2,  100)
            surface.blit(the_text, textRect)
            pos_of_click = ev.dict['pos']
            print(pos_of_click)
            getNameOfField(pos_of_click, x_offset_of_Board, y_offset_of_Board)


        # the_text = myFont.render(generateText(), True, (0, 30, 0))
        # surface.blit(the_text, (0, 0))
        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Change starting color on each row
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz+x_offset_of_Board, row*sq_sz+y_offset_of_Board, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                surface.blit(ball, ((col * sq_sz + 150+ball_offset), row * sq_sz + 150+ ball_offset))
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # for (col, row) in enumerate(the_board):
        #     surface.blit(ball, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))
        # the_board.insert(ball, (2,0))
        pygame.display.flip()  # displaying pygame window
    pygame.quit()


def getNameOfField(pos, offset_X, offset_Y):
    # letters = ["a", "b", "c", "d", "e", "f", "g"]
    # listWithFieldNames = [[]]
    # for rows in range (0, len(letters)):
    #     for col in range(0, len(letters)):
    #         listWithFieldNames[rows][col] = letters[rows]+str(col+1)
    # print(listWithFieldNames)

    if pos[0] > 150 and pos[0] < 210 and pos[1] >150 and pos[1] <210:
        print("A1")
    else:
        print("different field than a1")


def generateText(inp):
    if inp is not None:
        return inp
    return "Hello world!!"


if __name__ == "__main__":
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])


    # draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

    letters = ["a", "b", "c", "d", "e", "f", "g"]
    listWithFieldNames = np.ndarray((8,8), dtype=str)
    print(listWithFieldNames)
    # for rows in range(0, 7):
    #     for col in range(0, 7):
    #         listWithFieldNames. 'a'#str(letters[rows] + str(col))
    #         # listWithFieldNames.extend(letters[rows] + str(col + 1))
    listWithFieldNames[0][1] = 'B' + str(1)
    print(listWithFieldNames)