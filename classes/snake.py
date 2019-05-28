import pygame
from random import randint
from consts import *


class Snake:
    def __init__(self, canvas, game):
        self.canvas = canvas

        x = randint(0, (self.canvas.get_width() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
        y = randint(0, (self.canvas.get_height() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
        self.pieces = [(x, y)]
        self.speed = (0, 0)
        self.growing = False
        self.game = game

    def update(self, food):
        posToGrow = self.pieces[-1]
        self.move()
        if self.growing:
            self.pieces.append(posToGrow)
            self.growing = False
        self.eat(food)

    def move(self):
        for i in range(len(self.pieces) - 1, -1, -1):
            if i == 0:
                self.pieces[i] = (self.pieces[i][0] + self.speed[0], self.pieces[i][1] + self.speed[1])
            else:
                self.pieces[i] = self.pieces[i - 1]
        if self.dead():
            self.game.running = False

    def draw(self):
        pygame.draw.rect(self.canvas, (200, 200, 200), (self.pieces[0][0], self.pieces[0][1], TILE_SIZE, TILE_SIZE))
        for i in range(1, len(self.pieces)):
            pygame.draw.rect(self.canvas, (255, 255, 255), (self.pieces[i][0], self.pieces[i][1], TILE_SIZE, TILE_SIZE))

    def eat(self, food):
        if self.pieces[0][0] == food.pos()[0] and self.pieces[0][1] == food.pos()[1]:
            food.eat()
            self.growing = True

    def dead(self):
        return self.outOfScreen() or self.touchingTail()

    def touchingTail(self):
        return self.pieces[0] in self.pieces[1:]

    def outOfScreen(self):
        return (self.pieces[0][0] >= self.canvas.get_width() or
                self.pieces[0][1] >= self.canvas.get_height() or
                self.pieces[0][0] < 0 or
                self.pieces[0][1] < 0)

    def setSpeed(self, speed):
        self.speed = speed
