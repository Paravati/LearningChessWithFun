import pygame
import sys
import random
from pygame.locals import *

pygame.init()  # initiation of the pygame module

GAME_BOARD = pygame.display.set_mode((350, 350), 0, 32)   # initiation of the game window
pygame.display.set_caption('Tic tac toe, hello!')  # title of the game window

GAME_FIELD = [0, 0, 0,   # 0 - empty, 1 - user, 2 - computer
              0, 0, 0,   # game field is a list which describe status of the game board
              0, 0, 0]

MOVE = 1  # whose move is now: 1 - user, 2 - computer
WINNER = 0  # the result of the game: 0 - noone, 1 - user, 2 - computer, 3 - draw
WIN = False

# drawing of the game board
def draw_board():
    for i in range(0,3):  # x
        for j in range(0,3):  # y
            # arguments: surface, color, x, y, wight, height, thickness of the line
            pygame.draw.rect(GAME_BOARD, (255, 255, 255),
                             Rect((j * 50, i * 50), (50,50)), 1)

def draw_game_field():
    for i in range(0,3):
        for j in range(0,3):
            field = i * 3 + j  # field variable which takes values 0-8
            # x i y określają środki kolejnych pól,
            # a więc wartości: 25,25, 25,75 25,125 75,25 itd.
            x = j * 50 + 25
            y = i * 50 + 25

            if GAME_FIELD[field] == 1:
                # draw cicle
                pygame.draw.circle(GAME_BOARD, (0, 0, 255), (x, y), 10)
            elif GAME_FIELD[field] == 2:
                # draw computer circle
                pygame.draw.circle(GAME_BOARD, (255, 0, 0), (x, y), 10)
# pygame.display.get_active()

def make_move(field, MOVE):
    if GAME_FIELD[field] == 0:
        if MOVE == 1: # user move
            GAME_FIELD[field] = 1
            return 2
        elif MOVE == 2: # computer move
            GAME_FIELD[field] = 2
            return 1

    return MOVE

def check_field():
    pass
# main loop of the program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    GAME_BOARD.fill((0, 0, 0))  # definition of the surface colors in RGB palette
    draw_board()
    draw_game_field()
    pygame.display.update()
