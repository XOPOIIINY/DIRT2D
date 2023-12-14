import pygame
from settings import *
from tile import Tile
from player import Car


class Level:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_ind, row in enumerate(TEST_MAP):    # y position
            for col_ind, col in enumerate(row):     # x position
                x = col_ind * TILESIZE
                y = row_ind * TILESIZE
                if col == '1':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.car = Car((x // 32, y // 32), ANGLE, LENGTH, MAX_STEERING,
                                   MAX_ACCELERATION, MAX_SPEED, BRAKE_DECELERATION,
                                   FREE_DECELERATION, [self.visible_sprites])

    def run(self, game_time, screen):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(game_time, screen)
