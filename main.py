import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('DIRT 2D')
        self.clock = pygame.time.Clock()
        self.game_time = 0  # ingame deltatime, one of the most important variable in the project!
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.game_time = self.clock.get_time() / 1000
            self.screen.fill('black')
            self.level.run(self.game_time, self.screen)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()