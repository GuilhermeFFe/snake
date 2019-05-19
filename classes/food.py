import pygame
from consts import *
from random import randint


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = TILE_SIZE
        self.eaten = True
        self.x = None
        self.y = None
        self.update()

    def update(self):
        if self.eaten:
            self.x = randint(0, (self.canvas.get_width() - self.size)/TILE_SIZE)*TILE_SIZE
            self.y = randint(0, (self.canvas.get_height() - self.size)/TILE_SIZE)*TILE_SIZE
            self.eaten = False

    def draw(self):
        pygame.draw.rect(self.canvas, (255, 0, 0), (self.x, self.y, self.size, self.size))

    def eat(self):
        self.eaten = True

    def pos(self):
        return self.x, self.y
