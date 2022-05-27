import pygame
import os
import sys

from utility.config import get
from utility.button import Button
from utility.record_reader import get_records



WIDTH = get(os.path.join("utility", "settings.json"), "width")
HEIGHT = get(os.path.join("utility", "settings.json"), "height")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def records_menu():
    buttons_font = pygame.font.SysFont("comicsans", 70)
    records_font = pygame.font.SysFont("arial", 50)
    records = get_records()
    while True:
        WIN.blit(BACKGROUND, (0,0))
        
        y_pos = 150
        for record in records:
            record_label = records_font.render(record, 1, (255,255,255))
            WIN.blit(record_label, (WIDTH/2 - record_label.get_width()/2, y_pos))
            y_pos += 50
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        

        QUIT_BUTTON = Button(None, pos=(420,850), text_input='QUIT', font=buttons_font,
                             base_color='#d7fcd4', hovering_color='White')
        
        for button in [QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(WIN)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()