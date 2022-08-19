import os
import pygame
import codecs
from os import path

# Colour
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)

# Button Colours
LIGHT_COLOUR = (170, 170, 170)
DARK_COLOUR = (100, 100, 100)

# Window Sizes
WIDTH, HEIGHT = 1920, 1080
DS_WIDTH, DS_HEIGHT = 720, 405
SF = WIDTH / DS_WIDTH

# FPS
FPS = 120

# debug
debug = False

# files
GAME_FOLDER = path.dirname(__file__)
ASSETS_FOLDER = path.join(GAME_FOLDER, "assets")
BUTTONS_FOLDER = path.join(ASSETS_FOLDER, "buttonImages")

BUTTONS = {}

