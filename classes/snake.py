import pygame
from random import randint
from consts import *


class Snake:
    def __init__(self, game):
        self.game = game
        while True:
            x = randint(0, (self.game.canvas.get_width() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
            y = randint(0, (self.game.canvas.get_height() - TILE_SIZE)/TILE_SIZE)*TILE_SIZE
            if (x, y) not in self.game.wall.tiles:
                break
        self.pieces = [(x, y)]
        self.speed = (0, 0)
        self.growing = 0
        self.score = 0

    def update(self):
        posToGrow = self.pieces[-1]
        self.move()
        if self.growing:
            self.pieces.append(posToGrow)
            self.growing -= 1
        self.eat()

    def move(self):
        for i in range(len(self.pieces) - 1, -1, -1):
            if i == 0:
                self.pieces[i] = (self.pieces[i][0] + self.speed[0], self.pieces[i][1] + self.speed[1])
            else:
                self.pieces[i] = self.pieces[i - 1]
        if self.dead():
            self.game.running = False

    def draw(self):
        pygame.draw.rect(self.game.canvas, (200, 200, 200), (self.pieces[0][0]+1, self.pieces[0][1]+1, TILE_SIZE-2, TILE_SIZE-2))
        for i in range(1, len(self.pieces)):
            pygame.draw.rect(self.game.canvas, (255, 255, 255), (self.pieces[i][0]+1, self.pieces[i][1]+1, TILE_SIZE-2, TILE_SIZE-2))

    def eat(self):
        if self.pieces[0][0] == self.game.food.pos[0] and self.pieces[0][1] == self.game.food.pos[1]:
            self.game.food.eat()
            self.growing += GROW_BY
            self.score += 1

    def dead(self):
        return self.outOfScreen() or self.touchingTail() or self.touchingWall()

    def touchingWall(self):
        return self.pieces[0] in self.game.wall.tiles

    def touchingTail(self):
        return self.pieces[0] in self.pieces[1:]

    def outOfScreen(self):
        return (self.pieces[0][0] >= self.game.canvas.get_width() or
                self.pieces[0][1] >= self.game.canvas.get_height() or
                self.pieces[0][0] < 0 or
                self.pieces[0][1] < 0)

    def setSpeed(self, speed):
        self.speed = speed
