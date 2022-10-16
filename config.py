import os
from pygame.font import SysFont, init
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
YELLOW = (255,255,0)
ORANGE = (255, 191, 0)

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
TABLE_FOLDER = path.join(ASSETS_FOLDER, "table")
POCKET_FOLDER = path.join(ASSETS_FOLDER, "pocket")
CUEBALL_FOLDER = path.join(ASSETS_FOLDER, "cueball")
BALL_FOLDER = path.join(ASSETS_FOLDER, "balls")

BUTTONS = {}
TABLE_IMAGE = {}

# Values for balls (number, radius, friction and font)
# Need each colour twice for strips and solids (Excep black)
COLOUR = [YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN,
          BLACK, WHITE, YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN]
RADIUS = 5
FRICTION = 0
BALL_FONT = ("Agency FB", 10)
balls_potted = []
balls_notpotted = 15


#  Values needed for the pool table
RECT_HEIGHT = 600
CUSHIONS = 30
MARGIN = 30

#Cueball
CUEBALL_RADIUS = 5

#Variables for input box
COLOUR_OFF = WHITE
COLOUR_ON = YELLOW

init()
INPUT_FONT = SysFont(None, 32)
#Cushions coords

#Left side
CUSHION1 = (151, 110), (151, 295)
#Top left
CUSHION2 = (167, 103), (350, 103)
#Top Right
CUSHION3 = (369, 103), (552, 103)
#Right side
CUSHION4 = (559, 110), (559, 295)
#Bottom right
CUSHION5 = (369, 302), (552, 302)
#Bottom left
CUSHION6 = (167, 302), (350, 302)

#Backdround box for table friction
BOX_COORDS = (0, 0), (650, 370)

#Slowing balls down
SLOW_WHITE = pygame.time.get_ticks() + 1 * 1000
SLOW_RED = pygame.time.get_ticks() + 1 * 1000
SLOW_YELLOW = pygame.time.get_ticks() + 1 * 1000
SLOW_BLACK = pygame.time.get_ticks() + 1 * 1000

#Red ball coords
RED1 = (460, 202)