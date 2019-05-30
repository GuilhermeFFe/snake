from pygame.locals import *
from random import choice


class Computer:
    def __init__(self, game):
        self.game = game

    def play(self):
        keys = (K_UP, K_DOWN, K_LEFT, K_RIGHT)
        self.game.keyQueue.append(choice(keys))
