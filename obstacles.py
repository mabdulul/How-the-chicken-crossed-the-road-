import pygame as pg
from settings import *
import os
vec = pg.math.Vector2
screen = pg.display.set_mode((640, 480))

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")


class Obstacles(pg.sprite.Sprite):
    def __init__(self):
         pg.sprite.Sprite.__init__(self)
         self.image = pg.image.load(os.path.join(img_folder,"LeftSide_Walk2.png")).convert_alpha()
         self.image.set_colorkey((0,0,0))
         self.rect = self.image.get_rect()
         self.rect.centerx = WIDTH /2
         self.rect.bottom = HEIGHT - 2
         self.speedx = 0
    
    def update(self):
         self.speedx = 0
         keys = pg.key.get_pressed()  

         if keys[pg.K_LEFT]:
            self.speedx = -5
         if keys[pg.K_RIGHT]:
            self.speedx =  5
        
         self.rect.x += self.speedx
         #Stop the player from moving off the screen
         screen_rect = screen.get_rect()
         self.rect.clamp_ip(screen_rect)