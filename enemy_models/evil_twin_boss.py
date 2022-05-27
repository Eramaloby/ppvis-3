import pygame
import os

pygame.mixer.init()

from abstractions.laser import Laser
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

EVILTWIN = pygame.image.load(os.path.join("assets", "evil_twin_boss.png"))

EVILTWIN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_purple.png"))


class EvilTwin(Ship):
    def __init__(self):
        x = WIDTH / 2 - 100
        y = -200
        health = get(os.path.join("enemy_settings", "evil_twin_boss.json"), "health")
        vel = get(os.path.join("enemy_settings", "evil_twin_boss.json"), "vel")   
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img = EVILTWIN, EVILTWIN_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = get(os.path.join("enemy_settings", "evil_twin_boss.json"), "cooldown") 

    def move(self):
        self.y += self.vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 50, self.y + 150, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)
            
    def damage(self, dmg):
        self.health -= dmg