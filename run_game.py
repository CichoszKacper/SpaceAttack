import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# set up pygame

def run_game():
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.windowWidth, game_settings.windowHeight))
    pygame.display.set_caption("Space Attack")

    spaceship = Ship(game_settings, screen)

    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, spaceship, bullets)
        spaceship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, spaceship, bullets)


run_game()
