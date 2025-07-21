import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vec1 = self.velocity.rotate(random_angle)
        new_vec2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_count = 2
        count = new_asteroid_count

        for new in range(new_asteroid_count):
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            if new == 0:
                asteroid.velocity = new_vec1
                asteroid.velocity *= random.uniform(1, 2)
            else:
                asteroid.velocity = new_vec2
                asteroid.velocity *= random.uniform(1, 2)

