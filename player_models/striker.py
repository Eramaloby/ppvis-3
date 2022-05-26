import pygame
import os

pygame.mixer.init()

from abstractions.ship import Ship
from utility.config import get

HEIGHT = get(os.path.join("utility", "settings.json"), "height")
STRIKER = pygame.image.load(os.path.join("assets", "striker.png"))
STRIKER_LASER = pygame.image.load(os.path.join("assets", "striker_laser.png"))


class Striker(Ship):
    def __init__(self, x=300, y=630,
                 health=get(os.path.join("player_settings", "striker.json"), "health"),
                 vel = get(os.path.join("player_settings", "striker.json"), "vel")):
        super().__init__(x, y, health, vel)
        self.ship_img = STRIKER
        self.laser_img = STRIKER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.dmg = get(os.path.join("player_settings", "striker.json"), "dmg")
        self.laser_vel = -self.vel - 1
        self.cooldown = get(os.path.join("player_settings", "striker.json"), "cooldown")

    def move_lasers(self, objs):
        self.is_cooldown()
        for laser in self.lasers:
            laser.move(self.laser_vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.damage(self.dmg)
                        if obj.is_dead():
                            objs.remove(obj)
                            death_sound = pygame.mixer.Sound('music/explosion.wav')
                            pygame.mixer.Sound.play(death_sound)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
        
    def get_vel(self):
        return self.vel

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
        
    def get_vel(self):
        return self.vel