import pygame
import os
import random

pygame.mixer.init()

from abstractions.laser import Laser
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "kamikaze.png"))

BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))

class Kamikaze(Ship):
    def __init__(self):
        x = random.randrange(50, WIDTH-100)
        y = random.randrange(-1500, -100)
        health = get(os.path.join("enemy_settings", "kamikaze.json"), "health")
        vel = get(os.path.join("enemy_settings", "kamikaze.json"), "vel")   
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img = BLUE_SPACE_SHIP, BLUE_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = get(os.path.join("enemy_settings", "kamikaze.json"), "cooldown") 

    def move(self):
        self.y += self.vel

    def shoot(self):
        pass
            
    def damage(self, dmg):
        self.health -= dmg