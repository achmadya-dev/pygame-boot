import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from random import uniform
from pygame.math import Vector2
from typing import cast


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            radius=self.radius,
            width=LINE_WIDTH,
            center=self.position,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos = cast(Vector2, self.position)
        a1 = Asteroid(pos.x, pos.y, new_radius)
        a2 = Asteroid(pos.x, pos.y, new_radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
