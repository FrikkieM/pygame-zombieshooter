import pygame as pg 
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

        #Variables
        self.tilewidth = len(self.data[0])  #Length of one line
        self.tileheight = len(self.data)    #How many lines is it long...
        self.width = self.tilewidth * TILESIZE  #Get true width in pixels
        self.height = self.tileheight * TILESIZE

#https://youtu.be/3zV2ewk-IGU?list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i&t=312
class Camera:
    def __init__(self):