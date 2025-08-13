import pygame
import random
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, circle):
        pygame.draw.circle(circle, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(random_angle) *1.2
        velocity2 = self.velocity.rotate(-random_angle) *1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position[0], self.position[1]

        asteroid1 = Asteroid(x, y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(x, y, new_radius)
        asteroid2.velocity = velocity2
