import csv
from consts import *
from classes.wall import Wall


class Map:
    def __init__(self):
        with open(MAP_FILENAME) as file:
            self.mapData = list(csv.reader(file))
        self.height = len(self.mapData)*TILE_SIZE
        self.width = len(self.mapData[0])*TILE_SIZE

    def createWall(self, canvas):
        return Wall(self.mapData, canvas)
