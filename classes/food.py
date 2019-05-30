import pygame
from consts import *
from random import randint


class Food:
    def __init__(self, game):
        self.game = game
        self.eaten = True
        self.pos = (0, 0)
        self.update()

    def update(self):
        while self.eaten:
            self.pos = self.randomPos()
            self.eaten = self.pos in self.game.snake.pieces or self.pos in self.game.wall.tiles

    def draw(self):
        pygame.draw.rect(self.game.canvas, (255, 0, 0), (self.pos[0]+1, self.pos[1]+1, TILE_SIZE-2, TILE_SIZE-2))

    def eat(self):
        self.eaten = True

    def randomPos(self):
        x = randint(0, (self.game.canvas.get_width() - TILE_SIZE) / TILE_SIZE) * TILE_SIZE
        y = randint(0, (self.game.canvas.get_height() - TILE_SIZE) / TILE_SIZE) * TILE_SIZE
        return x, y
