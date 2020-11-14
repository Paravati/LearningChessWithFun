import pygame
import pygame_widgets as pw
from boardInitialisation import draw_board


def startGame():
    pygame.init()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 100, 220)
    backgroundIMG = pygame.image.load("images/background.jpeg")
    surface.fill(colorOfTheSurface)
    isNewGame = True
    myFont = pygame.font.SysFont("Courier", 30, bold=True)
    userPoints = 0
    swapSide = False
    randomSide = False
    return_to_menu = pw.Button(
        surface, 325, 550, 150, 75, text='Back to Menu',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )
    from_white = pw.Button(
        surface, 325, 200, 150, 55, text='White side',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('White mode')
    )
    from_black = pw.Button(
        surface, 325, 260, 150, 55, text='Black side',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Black mode')
    )
    random_side = pw.Button(
        surface, 325, 320, 150, 55, text='Random side',
        fontSize=20, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Random side mode')
    )
    while True:
        pygame.display.set_caption("Choose option")
        surface.fill(colorOfTheSurface)
        ev = pygame.event.poll()
        surface.blit(backgroundIMG, (0, 0))
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button is 1:  # left button of the mouse
                pos_of_click = ev.dict['pos']
                if return_to_menu.getX() < pos_of_click[0] < return_to_menu.getX() + return_to_menu.width and return_to_menu.getY() + return_to_menu.height > pos_of_click[1] > return_to_menu.getY():
                    break
                if isNewGame is True:
                    if from_white.getX() < pos_of_click[0] < from_white.getX() + from_white.width and from_white.getY()+from_white.height>pos_of_click[1]>from_white.getY():
                        from_white.onClick()
                        userPoints = draw_board([6, 4, 2, 0, 5, 7, 1, 3], swapSide=False, randomSwap=False)
                    elif from_black.getX() < pos_of_click[0] < from_black.getX() + from_black.width and from_black.getY()+from_black.height>pos_of_click[1]>from_black.getY():
                        from_black.onClick()
                        swapSide=True
                        userPoints = draw_board([6, 4, 2, 0, 5, 7, 1, 3], swapSide=True, randomSwap=False)
                    elif random_side.getX() < pos_of_click[0] < random_side.getX() + random_side.width and random_side.getY()+random_side.height>pos_of_click[1]>random_side.getY():
                        random_side.onClick()
                        randomSide=True
                        userPoints = draw_board([6, 4, 2, 0, 5, 7, 1, 3], swapSide=False, randomSwap=True)
                    # userPoints = draw_board([6, 4, 2, 0, 5, 7, 1, 3], swapSide=swapSide, randomSwap=randomSide)
                    isNewGame = False
                else:
                    userPoints = draw_board([6, 4, 2, 0, 5, 7, 1, 3], swapSide=swapSide, randomSwap=randomSide)

        if isNewGame is True:
            text = myFont.render("Choose option and click anywhere to start", True, (255, 255, 255))
            surface.blit(text, (100, 100))
            from_white.draw()
            from_black.draw()
            random_side.draw()
            return_to_menu.draw()
        if isNewGame is False:
            text = myFont.render("You lost! Click to try again", True, (255, 255, 255))
            surface.blit(text, (150, 100))
            text1 = myFont.render("Your score: " + str(userPoints), True, (255, 255, 255))
            surface.blit(text1, (250, 150))
            return_to_menu.draw()

        pygame.display.flip()  # displaying pygame window
    # pygame.quit()
