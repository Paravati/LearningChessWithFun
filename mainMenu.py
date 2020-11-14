import pygame
import pygame_widgets as pw
from trainMode import startGame


def mainMenu():
    pygame.init()
    surface = pygame.display.set_mode((800, 650))
    colorOfTheSurface = (0, 200, 120)
    surface.fill(colorOfTheSurface)
    titleIMG = pygame.image.load("images/mainTheme1.png")
    b_pawn = pygame.image.load("images/black_killer_pawn.png")
    isNewGame = True
    myFont = pygame.font.SysFont("Courier", 30, bold=True)
    start_button = pw.Button(
        surface, 250, 300, 250, 100, text='Train fields',
        fontSize=50, margin=20,
        inactiveColour=(100, 100, 100),
        pressedColour=(255, 0, 0), radius=14,
        onClick=lambda: print('Click')
    )
    while True:
        pygame.display.set_caption("menu")
        surface.fill(colorOfTheSurface)
        ev = pygame.event.poll()
        start_button.draw()
        surface.blit(pygame.transform.scale(titleIMG, (600,200)),(surface.get_height()/6, 50))
        surface.blit(pygame.transform.scale(b_pawn, (350,400)), (550,surface.get_width()/3))
        surface.blit(pygame.transform.scale(b_pawn, (350,400)), (0,surface.get_height()-110))
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
