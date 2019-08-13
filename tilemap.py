import pygame as pg 
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        #Variables
        self.tilewidth = len(self.data[0])  #Length of one line
        self.tileheight = len(self.data)    #How many lines is it long...
        self.width = self.tilewidth * TILESIZE  #Get true width in pixels
        self.height = self.tileheight * TILESIZE

#https://youtu.be/3zV2ewk-IGU?list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i&t=312
class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)