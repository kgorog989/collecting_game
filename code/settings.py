import pygame 
from os.path import join 
from os import mkdir
from timer import Timer

WINDOW_WIDTH, WINDOW_HEIGHT = 800,520 
TILE_SIZE = 16
PLAYER_SIZE = 48
COW_SIZE = 32
HEART_SIZE = 50
SCALING_FACTOR = 4

GAME_DATA = {'running': True, 'highscore': 0, 'score': 0, 'health': 3}

FONT_SIZE = 60
FONT_COLOR = (110, 86, 43)

WATER_COLOR = '#9bd4c3'