import pygame, os
from settings import *


class Land:
    def __init__(self):
        self.width = land_width
        self.height = land_height
        self.x = land_x
        self.y = land_y
        self.image = pygame.image.load(os.path.join('assets', 'land.png')).convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surface, x):
        for i in range(2):
            surface.blit(self.image, (x + self.width * i, self.y))

    def update(self):
        self.x -= 5 * dt
        if self.x <= -self.width:
            self.x = 0
