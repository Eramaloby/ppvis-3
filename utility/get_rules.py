import pygame
import os
import sys

from utility.config import get
from utility.button import Button

WIDTH = get(os.path.join("utility", "settings.json"), "width")
HEIGHT = get(os.path.join("utility", "settings.json"), "height")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def get_rules():
    rules = ''
    with open(os.path.join('utility', 'rules.txt'), 'r') as f:
        try:
            rules = f.read()
        except:
            rules = 'Have fun!'
            
    return rules
    
    
                