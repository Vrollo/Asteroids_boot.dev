import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.velocity.x > 0 and (self.position.x >= SCREEN_WIDTH + self.radius):
            self.position.x = -self.radius
        elif self.velocity.x < 0 and (self.position.x <= -self.radius):
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.velocity.y > 0 and (self.position.y >= SCREEN_HEIGHT + self.radius):
            self.position.y= -self.radius
        elif self.velocity.y < 0 and (self.position.y <= -self.radius):
            self.position.y = SCREEN_HEIGHT + self.radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(new_angle)
            new_vector2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2