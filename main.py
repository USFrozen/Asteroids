# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    font = pygame.font.Font(None, 24)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    # Primary game loop
    # Allows quitting game through X button, Alt F4, and other methods
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if player.hit(asteroid):
                print(f"Game over!, Score: {score}")
                sys.exit()

            for shot in shots:
                if asteroid.hit(shot):
                    asteroid.split()
                    shot.kill()
                    score += 100

        # Screen
        screen.fill("black")

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        for sprite in drawable:
            sprite.draw(screen)

        # Flips frame buffer to next frame (default 60 FPS)
        pygame.display.flip()

        # Ticks game loop, pauses for (default) 1/60th of a second, sets Delta Time in MS
        dt = (clock.tick(FRAMERATE) / 1000)

# Makes it so main loop doesnt run if main.py is imported elsewhere
if __name__ == "__main__":
    main()

