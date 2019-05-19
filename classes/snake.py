import pygame
from consts import *


class Snake:
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.pieces = [pos]
        self.velocity = (TILE_SIZE, 0)

    def update(self):
        for i in range(len(self.pieces) - 1, -1, -1):
            if i == 0:
                self.pieces[i] = (self.pieces[i][0] + self.velocity[0], self.pieces[i][1] + self.velocity[1])
            else:
                self.pieces[i] = self.pieces[i - 1]

    def draw(self):
        for piece in self.pieces:
            pygame.draw.rect(self.canvas, (255, 255, 255), (piece[0], piece[1], TILE_SIZE, TILE_SIZE))
