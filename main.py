# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# Imports game constants from local constants.py
from constants import *
# Imports player from local player.py
from player import *

def main():
    # Startup messages, shows game resolution
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initalizes pygame
    pygame.init()

    # Sets pygame display to use SCREEN_WIDTH and SCREEN_HEIGHT from constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Sets pygame clock, used for game tick function
    clock = pygame.time.Clock()

    # Sets game FPS limit to 60 to limit resource usage. Pauses game tick for 1/60th of a second
    fps = 60

    # Delta Time, time since last tick happened in miliseconds
    dt = 0

    # Draw player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Primary game loop
    # Allows quitting game through X button, Alt F4, and other methods
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fills screen with black color
        screen.fill((0,0,0))

        # Draw player on screen
        player.draw(screen)

        # Flips frame buffer to next frame (default 60 FPS)
        pygame.display.flip()


        # Ticks game loop, pauses for (default) 1/60th of a second, sets Delta Time in MS
        dt = (clock.tick(fps) / 1000)

# Makes it so main loop doesnt run if main.py is imported elsewhere
if __name__ == "__main__":
    main()

