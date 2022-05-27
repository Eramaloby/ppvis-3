import pygame
import os
import random
import sys
pygame.font.init()
pygame.mixer.init()

from player_models.player import Player
from player_models.twingun import TwinGun
from player_models.striker import Striker

from enemy_models.shift import Shift
from enemy_models.enemy import Enemy
from enemy_models.kamikaze import Kamikaze
from enemy_models.diagonal import Diagonal
from enemy_models.moon_boss import Moon
from enemy_models.wall_boss import Wall
from enemy_models.two_face_boss import TwoFace
from enemy_models.evil_twin_boss import EvilTwin

from abstractions.collide import collide
from utility.config import get 
from utility.reader import read
from utility.button import Button

WIDTH, HEIGHT = get(os.path.join("utility", "settings.json"), "width"), get(os.path.join("utility", "settings.json"), "width")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))



def game():
    run = True
    FPS = get(os.path.join("utility", "settings.json"), "fps")

    level = get(os.path.join("utility", "settings.json"), "level")
    lives = get(os.path.join("utility", "settings.json"), "lives")
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    
    waves = read(os.path.join("utility", "waves.json"))
    enemies = []

    player = Striker()

    clock = pygame.time.Clock()

    lost = False
    

    
    
    pygame.mixer.music.load("music/main.wav")
    pygame.mixer.music.play(-1)
    
    def redraw_window():
        WIN.blit(BACKGROUND, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_sound = pygame.mixer.Sound('music/lost.wav')
            pygame.mixer.Sound.play(lost_sound)
            while lost:
                WIN.blit(BACKGROUND, (0,0))
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                buttons_font = pygame.font.SysFont("comicsans", 70)
                QUIT_BUTTON = Button(None, pos=(420,850), text_input='QUIT', font=buttons_font,
                             base_color='#d7fcd4', hovering_color='White')
                lost_label = lost_font.render("You Lost!", 1, (255,255,255))
                WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
                QUIT_BUTTON.change_color(MENU_MOUSE_POS)
                QUIT_BUTTON.update(WIN)
                
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

    while run:
        for wave in waves:
            clock.tick(FPS)
            redraw_window()

            if lives <= 0 or player.is_dead():
                lost = True

            

            if len(enemies) == 0:
                level += 1
                for name in wave:
                    if name == 'red':
                        enemies.append(Enemy('red'))
                    elif name == 'green':
                        enemies.append(Enemy('green'))
                    elif name == 'purple':
                        enemies.append(Enemy('purple'))
                    elif name == 'kamikaze':
                        enemies.append(Kamikaze())
                    elif name == 'shift':
                        enemies.append(Shift())
                    elif name == 'diagonal':
                        enemies.append(Diagonal())
                    elif name == 'moon':
                        enemies.append(Moon())
                    elif name == 'wall':
                        enemies.append(Wall())
                    elif name == 'two_face':
                        enemies.append(TwoFace())
                    elif name == 'evil_twin':
                        enemies.append(EvilTwin())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            player_vel = player.get_vel()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - player_vel > 0: # left
                player.x -= player_vel
            if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
                player.x += player_vel
            if keys[pygame.K_w] and player.y - player_vel > 0: # up
                player.y -= player_vel
            if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
                player.y += player_vel
            if keys[pygame.K_SPACE]:
                player.shoot()

            for enemy in enemies[:]:
                enemy.move()
                enemy.move_lasers(player)

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)

            player.move_lasers(enemies)
