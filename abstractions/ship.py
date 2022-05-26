import os
import pygame

pygame.mixer.init()

from abstractions.laser import Laser
from utility.config import get


HEIGHT = get(os.path.join("utility", "settings.json"), "height")

class Ship:

    def __init__(self, x, y, health=100, vel=5):
        self.x = x
        self.y = y
        self.health = health
        self.vel = vel
        self.ship_img = None
        self.laser_vel = vel + 1
        self.laser_img = None
        self.lasers = []
        self.cooldown = 30
        
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, obj):
        self.is_cooldown()
        for laser in self.lasers:
            laser.move(self.laser_vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def is_cooldown(self):
        if self.cool_down_counter >= self.cooldown:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)

    def is_dead(self):
        return self.health <= 0

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()