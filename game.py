import pygame
from pygame.locals import *
from classes import *
from consts import *
from time import sleep


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.canvas = None
        self.food = None
        self.snake = None

    def run(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('game')

        self.food = Food(self.canvas)
        self.snake = Snake(self.canvas, (0, 0))
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
        self.snake.update()

    def render(self):
        self.canvas.fill((0, 0, 0))
        self.food.draw()
        self.snake.draw()


if __name__ == '__main__':
    game = Game(400, 300)
    game.run()
