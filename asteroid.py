from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        spawn_1_velocity = self.velocity.rotate(new_angle)
        spawn_2_velocity = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_1.velocity = spawn_1_velocity * 1.2
        spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_2.velocity = spawn_2_velocity * 1.2

