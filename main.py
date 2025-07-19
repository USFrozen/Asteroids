# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Primary game loop
    # Allows quitting game through X button, Alt F4, and other methods
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen draw and update
        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)

        # Flips frame buffer to next frame (default 60 FPS)
        pygame.display.flip()

        # Ticks game loop, pauses for (default) 1/60th of a second, sets Delta Time in MS
        dt = (clock.tick(FRAMERATE) / 1000)

# Makes it so main loop doesnt run if main.py is imported elsewhere
if __name__ == "__main__":
    main()

