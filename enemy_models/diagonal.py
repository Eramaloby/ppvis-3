import pygame
import os
import random

pygame.mixer.init()

from abstractions.diagonal_laser_right import DiagonalLaserRight
from abstractions.diagonal_laser_left import DiagonalLaserLeft
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

DIAGONAL = pygame.image.load(os.path.join("assets", "diagonal.png"))

DIAGONAL_LASER_L = pygame.image.load(os.path.join("assets", "diagonal_laser_left.png"))
DIAGONAL_LASER_R = pygame.image.load(os.path.join("assets", "diagonal_laser_right.png"))


class Diagonal(Ship):
    def __init__(self):
        x = random.randrange(50, WIDTH-100)
        y = random.randrange(-1500, -100)
        health = get(os.path.join("enemy_settings", "diagonal.json"), "health")
        vel = get(os.path.join("enemy_settings", "diagonal.json"), "vel")   
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img, self.laser_img_r = DIAGONAL, DIAGONAL_LASER_L, DIAGONAL_LASER_R
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = get(os.path.join("enemy_settings", "diagonal.json"), "cooldown") 

    def move(self):
        self.y += self.vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser_left = DiagonalLaserLeft(self.x-20, self.y, self.laser_img)
            laser_right = DiagonalLaserRight(self.x-20, self.y, self.laser_img_r)
            self.lasers.append(laser_left)
            self.lasers.append(laser_right)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)
            
    def damage(self, dmg):
        self.health -= dmg