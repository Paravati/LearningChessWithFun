import pygame
import pygame_widgets as pw
from trainMode import startGame


def mainMenu():
    pygame.init()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 200, 120)
    surface.fill(colorOfTheSurface)
    # titleIMG = pygame.image.load("images/mainTheme1.png")
    backgroundIMG = pygame.image.load("images/chessMainMenu.jpg")
    isNewGame = True
    myFont = pygame.font.SysFont("Courier", 30, bold=True)
    start_button = pw.Button(
        surface, 230, 150, 350, 100, text='TRAIN FIELDS',
        fontSize=40, margin=20,
        inactiveColour=(110, 110, 110),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )
    gameplay_button = pw.Button(
        surface, 230, 270, 350, 100, text='PLAY THE GAME',
        fontSize=40, margin=20,
        inactiveColour=(110, 110, 110),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )
    learn_tactics = pw.Button(
        surface, 230, 390, 350, 100, text='LEARN TACTICS',
        fontSize=40, margin=20,
        inactiveColour=(110, 110, 110),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )
    while True:
        pygame.display.set_caption("menu")
        surface.fill(colorOfTheSurface)
        surface.blit(pygame.transform.scale(backgroundIMG, (800,650)), (0,0))
        ev = pygame.event.poll()
        start_button.draw()
        gameplay_button.draw()
        learn_tactics.draw()
        # surface.blit(pygame.transform.scale(titleIMG, (600,200)),(surface.get_height()/6, 50))
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos_of_click = ev.dict['pos']
            if start_button.getX() < pos_of_click[0] < start_button.getX() + start_button.width and start_button.getY() + start_button.height > pos_of_click[1] > start_button.getY():
                startGame()
        pygame.display.flip()  # displaying pygame window

    pygame.quit()


if __name__ == "__main__":
    mainMenu()
