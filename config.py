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
debug = True

# files
GAME_FOLDER = path.dirname(__file__)
ASSETS_FOLDER = path.join(GAME_FOLDER, "assets")
BUTTONS_FOLDER = path.join(ASSETS_FOLDER, "buttonImages")
TABLE_FOLDER = path.join(ASSETS_FOLDER, "table")
POCKET_FOLDER = path.join(ASSETS_FOLDER, "pocket")
CUEBALL_FOLDER = path.join(ASSETS_FOLDER, "cueball")
BALL_FOLDER = path.join(ASSETS_FOLDER, "balls")
CUESTICK_FOLDER = path.join(ASSETS_FOLDER, "cuestick")
CUE_IMAGE_ = pygame.image.load(path.join(CUESTICK_FOLDER, "cue.png"))
#CUE_IMAGE_SCALED = pygame.transform.rotozoom(CUE_IMAGE_ORIGINAL, 0, 0.09)

BUTTONS = {}
TABLE_IMAGE = {}

RADIUS = 5
FRICTION = 0
BALL_FONT = ("Agency FB", 10)
balls_potted = []
balls_notpotted = 15


#Values needed for the pool table
RECT_HEIGHT = 600
CUSHIONS = 30
MARGIN = 30

#Cueball
BALL_RADIUS = 5

#Variables for input box
COLOUR_OFF = WHITE
COLOUR_ON = YELLOW

init()
INPUT_FONT = SysFont(None, 32)
#Cushions coords

#Left side
CUSHION1 = (153, 110), (153, 295)
#Top left
CUSHION2 = (167, 101), (350, 101)
#Top Right
CUSHION3 = (369, 101), (552, 101)
#Right side
CUSHION4 = (557, 110), (557, 295)
#Bottom right
CUSHION5 = (369, 299), (552, 299)
#Bottom left
CUSHION6 = (167, 299), (350, 299)

#Backdround box for table friction
BOX_COORDS = (0, 0), (650, 370)

#Slowing balls down
SLOW_BALL = pygame.time.get_ticks() + 1 * 1000

#Red ball coords
RED1 = (483, 204)
RED2 = (492, 190)
RED3 = (501, 214)
RED4 = (501, 194)
RED5 = (511, 180)
RED6 = (511, 199)
RED7 = (511, 209)

#Yellow ball coords
Yellow1 = (474, 199)
Yellow2 = (483, 194)
Yellow3 = (492, 209)
Yellow4 = (502, 204)
Yellow5 = (504, 184)
Yellow6 = (511, 190)
Yellow7 = (511, 219)

#Black ball Coord
Black1 = (492, 199)

#Corner pocket radius, coords
POCKET_RADIUS = 14.5
pocket_coords = [ 
    (150, 93), #Top left
    (560, 93), #Top right
    (150, 312), #Bottom left
    (560, 312), #Bottom right
    (359, 85), #Top middle
    (359, 321) #Bottom middle
]
CP_TL = (150, 93)
CP_TR = (560, 93)
CP_BL = (150, 312)
CP_BR = (560, 312)
MP_T = (359, 93)
MP_B = (359, 312)


#Cue variables
FORCE = 100
MAX_FORCE = 19000
DIRECTION = 1



#Balls postted coordinates
REDS = [(187, 342), (202, 342), (218, 342), (235, 342), (251, 342), (267, 342), (280, 342)]
YELLOWS = [(187, 362), (202, 362), (218, 362), (235, 362), (251, 362), (267, 362), (280, 362)]





#Coords needed for the level

L_RED1 = (547, 113)
L_RED2 = (547, 291)
L_RED3 = (359, 113)
L_RED4 = (359, 291)
L_RED5 = (174, 113)
L_RED6 = (174, 291)