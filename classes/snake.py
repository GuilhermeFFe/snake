import pygame
from consts import *


class Snake:
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.pieces = [pos]
        self.speed = (TILE_SIZE, 0)
        self.growing = False

    def update(self, food):
        posToGrow = self.pieces[-1]
        for i in range(len(self.pieces) - 1, -1, -1):
            if i == 0:
                self.pieces[i] = (self.pieces[i][0] + self.speed[0], self.pieces[i][1] + self.speed[1])
            else:
                self.pieces[i] = self.pieces[i - 1]
        if self.growing:
            self.pieces.append(posToGrow)
            self.growing = False
        self.eat(food)

    def draw(self):
        for piece in self.pieces:
            pygame.draw.rect(self.canvas, (255, 255, 255), (piece[0], piece[1], TILE_SIZE, TILE_SIZE))

    def eat(self, food):
        if self.pieces[0][0] == food.pos()[0] and self.pieces[0][1] == food.pos()[1]:
            food.eat()
            self.growing = True

    def setSpeed(self, speed):
        self.speed = speed
