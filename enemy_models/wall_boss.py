import pygame
import os

pygame.mixer.init()

from abstractions.laser import Laser
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

WALL = pygame.image.load(os.path.join("assets", "wall_boss.png"))

WALL_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))


class Wall(Ship):
    def __init__(self):
        x = WIDTH / 2 - 50
        y = 10
        health = get(os.path.join("enemy_settings", "wall_boss.json"), "health")
        vel = get(os.path.join("enemy_settings", "wall_boss.json"), "vel")   
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img = WALL, WALL_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = get(os.path.join("enemy_settings", "wall_boss.json"), "cooldown") 

    def move(self):
        self.y += self.vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser_mid = Laser(self.x + 50, self.y, self.laser_img)
            laser_left = Laser(self.x, self.y, self.laser_img)
            laser_right = Laser(self.x + 100, self.y, self.laser_img)
            self.lasers.append(laser_mid)
            self.lasers.append(laser_left)
            self.lasers.append(laser_right)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)
            
    def damage(self, dmg):
        self.health -= dmg