import pygame
import os
import random

pygame.mixer.init()

from abstractions.laser import Laser
from abstractions.ship import Ship
from utility.config import get

WIDTH = get(os.path.join("utility", "settings.json"), "width")

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PURPLE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_purple.png"))

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PURPLE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_purple.png"))


class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "purple": (PURPLE_SPACE_SHIP, PURPLE_LASER)
            }

    def __init__(self, name: str):
        if name == "red":
            health = get(os.path.join("enemy_settings", "red.json"), "health")
            vel = get(os.path.join("enemy_settings", "red.json"), "vel")
            ship_img, laser_img = self.COLOR_MAP["red"]
            cooldown = get(os.path.join("enemy_settings", "red.json"), "cooldown")
            
        elif name == "green":    
            health = get(os.path.join("enemy_settings", "green.json"), "health")
            vel = get(os.path.join("enemy_settings", "green.json"), "vel")
            ship_img, laser_img = self.COLOR_MAP["green"]
            cooldown = get(os.path.join("enemy_settings", "green.json"), "cooldown")
            
        elif name == "purple":    
            health = get(os.path.join("enemy_settings", "purple.json"), "health")
            vel = get(os.path.join("enemy_settings", "purple.json"), "vel")
            ship_img, laser_img = self.COLOR_MAP["purple"]
            cooldown = get(os.path.join("enemy_settings", "purple.json"), "cooldown")
        
        x = random.randrange(50, WIDTH-100)
        y = random.randrange(-1500, -100)    
        super().__init__(x, y, health, vel)
        self.ship_img, self.laser_img = ship_img, laser_img
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.cooldown = cooldown

    def move(self):
        self.y += self.vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)
            
    def damage(self, dmg):
        self.health -= dmg