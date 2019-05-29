import pygame
from consts import TILE_SIZE


class Wall:
    def __init__(self, mapData, canvas):
        self.canvas = canvas
        self.tiles = []
        for i in range(len(mapData)):
            for j in range(len(mapData[i])):
                if mapData[i][j] == '1':
                    self.tiles.append((j*TILE_SIZE, i*TILE_SIZE))

    def draw(self):
        for tile in self.tiles:
            pygame.draw.rect(self.canvas, (0, 0, 255), (tile[0], tile[1], TILE_SIZE, TILE_SIZE))
