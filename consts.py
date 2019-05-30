DIFFICULTY = 8
TILE_SIZE = 15
MAP_FILENAME = './maps/wall.csv'
COMPUTER_PLAYING = True

FRAME_RATE = 2*DIFFICULTY
GROW_BY = int(DIFFICULTY/3)
DOWN = (0, TILE_SIZE)
UP = (0, -TILE_SIZE)
LEFT = (-TILE_SIZE, 0)
RIGHT = (TILE_SIZE, 0)
