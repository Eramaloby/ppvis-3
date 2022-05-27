import pygame
import os

pygame.mixer.init()

from utility.config import get
from abstractions.ship import Ship
from abstractions.laser import Laser

HEIGHT = get(os.path.join("utility", "settings.json"), "height")
TWINGUN = pygame.image.load(os.path.join("assets", "twingun_player.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))


class TwinGun(Ship):
    def __init__(self, x=350, y=630,
                 health=get(os.path.join("player_settings", "twingun.json"), "health"),
                 vel=get(os.path.join("player_settings", "twingun.json"), "vel")):
        super().__init__(x, y, health, vel)
        self.ship_img = TWINGUN
        self.laser_img = YELLOW_LASER
        self.dmg = get(os.path.join("player_settings", "twingun.json"), "dmg")
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.laser_vel = -self.vel - 1
        self.cooldown = get(os.path.join("player_settings", "twingun.json"), "cooldown")
                            
    def shoot(self):
        if self.cool_down_counter == 0:
            laser_left = Laser(self.x + 10, self.y, self.laser_img)
            laser_right = Laser(self.x - 10, self.y, self.laser_img)
            self.lasers.append(laser_left)
            self.lasers.append(laser_right)
            self.cool_down_counter = 1
            shot_sound = pygame.mixer.Sound('music/laser.wav')
            pygame.mixer.Sound.play(shot_sound)
            
            
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

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
        
    def get_vel(self):
        return self.vel