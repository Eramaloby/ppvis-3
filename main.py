import pygame
import os
import sys

pygame.mixer.init()

from game import game
from utility.config import get
from utility.button import Button
from rules import rules_menu

WIDTH = get(os.path.join("utility", "settings.json"), "width")
HEIGHT = get(os.path.join("utility", "settings.json"), "height")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    title_font = pygame.font.SysFont("comicsans", 70)
    
    pygame.mixer.music.load("music/menu.wav")
    pygame.mixer.music.play(-1)
    while True:
        WIN.blit(BACKGROUND, (0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        PLAY_BUTTON = Button(None, pos=(420,250), text_input='PLAY', font=title_font,
                             base_color='#d7fcd4', hovering_color='White')
        
        RULES_BUTTON = Button(None, pos=(420,400), text_input='RULES', font=title_font,
                             base_color='#d7fcd4', hovering_color='White')
        
        QUIT_BUTTON = Button(None, pos=(420,700), text_input='QUIT', font=title_font,
                             base_color='#d7fcd4', hovering_color='White')
        
        
        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(WIN)
            
        
        
        #title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        
        #WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game()
                if RULES_BUTTON.check_for_input(MENU_MOUSE_POS):
                    rules_menu()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
    
main()