import pygame
from circleshape import CircleShape

SHOT_RADIUS = 5

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, bullet):
        pygame.draw.circle(bullet, "teal", self.position, self.radius)