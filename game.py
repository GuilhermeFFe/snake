import pygame
from pygame.locals import *
from classes import Food
from consts import *
from time import sleep


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.canvas = None
        self.food = None

    def run(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('game')

        self.food = Food(self.canvas)
        self.gameLoop()

        pygame.quit()
        exit(0)

    def gameLoop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.tick()
            self.render()
            pygame.display.update()
            sleep(1 / FRAME_RATE)

    def tick(self):
        self.food.update()

    def render(self):
        self.canvas.fill((0, 0, 0))
        self.food.draw()


if __name__ == '__main__':
    game = Game(400, 300)
    game.run()
