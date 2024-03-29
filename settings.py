import pygame as pg
vec = pg.math.Vector2

#define some colors (R,G,B)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024    # 16*64 or 32*32 or 64*16
HEIGHT = 768    # 16*48 or 32*24 or 64*12
FPS = 60
TITLE = "Basic PyGame"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'element_green_square_glossy.png'


# player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
BARREL_OFFSET = vec(30, 10)


# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 300
KICKBACK = 200
GUN_SPREAD = 5


# Mob Settings
MOB_IMG = 'zoimbie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0,0,30,30)
