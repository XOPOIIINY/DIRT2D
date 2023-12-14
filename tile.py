import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_groups):
        super().__init__(sprite_groups)
        self.image = pygame.image.load('Tiles/road(32).jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
