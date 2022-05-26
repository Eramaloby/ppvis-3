import pygame
import os
import random

pygame.mixer.init()

from abstractions.laser import Laser
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

SHIFT = pygame.image.load(os.path.join("assets", "shift.png"))

SHIFT_LASER = pygame.image.load(os.path.join("assets", "shift.png"))

class Shift(Ship):
    def __init__(self):
        x = random.randrange(50, WIDTH-100)
        y = random.randrange(-1500, -100)
        health = get(os.path.join("enemy_settings", "shift.json"), "health")
        vel = get(os.path.join("enemy_settings", "shift.json"), "vel")   
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img = SHIFT, SHIFT_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = get(os.path.join("enemy_settings", "shift.json"), "cooldown") 

    def move(self):
        self.y += self.vel
        self.x += random.choice([-2, 2])

    def shoot(self):
        pass
            
    def damage(self, dmg):
        self.health -= dmg