import pygame
from consts import *
from random import randint


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.eaten = True
        self.x = None
        self.y = None
        self.update(None)

    def update(self, snake):
        while self.eaten:
            self.x = randint(0, (self.canvas.get_width() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
            self.y = randint(0, (self.canvas.get_height() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
            self.eaten = snake is not None and (self.x, self.y) in snake.pieces

    def draw(self):
        pygame.draw.rect(self.canvas, (255, 0, 0), (self.x, self.y, TILE_SIZE, TILE_SIZE))

    def eat(self):
        self.eaten = True

    def pos(self):
        return self.x, self.y
