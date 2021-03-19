import pygame
import os
import random
import time



BREDDE,HØYDE = 750,750
VINDU = pygame.display.set_mode((BREDDE,HØYDE))
pygame.display.set_caption("Romangrep")



# Laste bilder
RØD_ROMSKIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GRØNN_ROMSKIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLÅ_ROMSKIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#Spiller skip
GUL_ROMSKPIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Lasere
RØD_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GRØN_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLÅ_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
GUL_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

#Bakgrunnen
BG =  pygame.image.load(os.path.join("assets","background-black.png"))

