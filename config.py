import os
from pygame.font import SysFont, init
import pygame
import codecs
from os import path
import random

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
CUESTICK_FOLDER = path.join(ASSETS_FOLDER, "cuestick")
SETTINGS_IMAGES_FOLDER = path.join(BUTTONS_FOLDER, "Settings")
#CUE_IMAGE_ = pygame.image.load(path.join(CUESTICK_FOLDER, "cue.png"))
#CUE_IMAGE_SCALED = pygame.transform.rotozoom(CUE_IMAGE_ORIGINAL, 0, 0.09)

BUTTONS = {}
TABLE_IMAGE = {}

RADIUS = 5
FRICTION = 0
BALL_FONT = ("Agency FB", 10)
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
CUSHION1 = (156, 116), (156, 289)
#Top left
CUSHION2 = (173, 99), (348, 99)
#Top Right
CUSHION3 = (370, 99), (546, 99)
#Right side
CUSHION4 = (554, 116), (554, 289)
#Bottom right
CUSHION5 = (370, 298), (546, 298)
#Bottom left
CUSHION6 = (173, 298), (348, 298)

#Coords for cusions surrounding pockets
S_CP_TL_1 = (155, 116), (152, 110)
S_CP_TL_2 = (173, 98), (167, 95)
S_MP_T_1 = (348, 98), (349, 95)
S_MP_T_2 = (370, 98), (369, 95)
S_CP_TR_1 = (555, 116), (566, 110)
S_CP_TR_2 = (546, 98), (552, 95)
S_CP_BR_1 = (555, 289), (566, 294)
S_CP_BR_2 = (546, 299), (552, 308)
S_MP_B_1 = (348, 299), (349, 309)
S_MP_B_2 = (370, 299), (369, 308)
S_CP_BL_1 = (155, 289), (152, 294)
S_CP_BL_2 = (173, 299), (167, 308)


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
POCKET_RADIUS = 21
pocket_coords = [ 
    (150, 93), #Top left
    (569, 93), #Top right
    (150, 312), #Bottom left
    (569, 312), #Bottom right
    (359, 85), #Top middle
    (359, 321) #Bottom middle
]
CP_TL = (150, 93)
CP_TR = (569, 93)
CP_BL = (150, 312)
CP_BR = (570, 312)
MP_T = (359, 93)
MP_B = (359, 312)


#Cue variables
FORCE = 8000
MAX_FORCE = 19000
DIRECTION = 1



#Balls postted coordinates
REDS = (187, 342)
YELLOWS = (187, 362)



