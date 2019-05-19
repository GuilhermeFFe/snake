import pygame
from pygame.locals import *
from consts import *
from time import sleep


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.canvas = None

    def run(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('game')

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.tick()
            self.render()
            pygame.display.update()
            sleep(1/FRAME_RATE)

        pygame.quit()
        exit(0)

    def tick(self):
        pass

    def render(self):
        pass


if __name__ == '__main__':
    game = Game(400, 300)
    game.run()
