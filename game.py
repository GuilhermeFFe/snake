import pygame
from pygame.locals import *
from classes import *
from consts import *
from time import sleep


class Game:
    def __init__(self):
        self.running = False
        self.canvas = None
        self.food = None
        self.snake = None
        self.map = None
        self.wall = None
        self.keyQueue = []

    def run(self):
        pygame.init()
        self.map = Map()
        self.canvas = pygame.display.set_mode((self.map.width, self.map.height))
        pygame.display.set_caption('game')

        self.wall = self.map.createWall(self)
        self.snake = Snake(self)
        self.food = Food(self)
        self.gameLoop()

        pygame.quit()

    def gameLoop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    self.keyQueue.append(event.key)
            self.tick()
            self.render()
            pygame.display.update()
            sleep(1 / FRAME_RATE)

        print('You died, idiot!')
        print('Score: ', self.snake.score)

    def moveSnake(self, key):
        if key == K_DOWN:
            if self.snake.speed != UP:
                self.snake.setSpeed(DOWN)
        if key == K_UP:
            if self.snake.speed != DOWN:
                self.snake.setSpeed(UP)
        if key == K_RIGHT:
            if self.snake.speed != LEFT:
                self.snake.setSpeed(RIGHT)
        if key == K_LEFT:
            if self.snake.speed != RIGHT:
                self.snake.setSpeed(LEFT)

    def tick(self):
        if len(self.keyQueue) > 0:
            self.moveSnake(self.keyQueue.pop(0))
        self.food.update()
        self.snake.update()

    def render(self):
        self.canvas.fill((0, 0, 0))
        self.food.draw()
        self.snake.draw()
        self.wall.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
