import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 100, 150, 90)
    some_color = (255, 45, 255)        # A color is a mix of (Red, Green, Blue)
    i = 0
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)
        ball = pygame.image.load('ball.png')
        main_surface.blit(ball, (100, 120))

        myFont = pygame.font.SysFont("Courier", 16)
        the_text = myFont.render("Hello world!" + str(i), True, (0,0,0))
        main_surface.blit(the_text, (0,0))
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        i+=1

    pygame.quit()     # Once we leave the loop, close the window.

main()