import sys

import pygame

from bullet import Bullet
from settings import Settings


def check_events(game_settings, screen, spaceship, bullets):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, spaceship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)


def check_keydown_events(event, game_settings, screen, spaceship, bullets):
    if event.key == pygame.K_DOWN:
        spaceship.rect.centery += 2
        spaceship.moving_down = True
    elif event.key == pygame.K_UP:
        spaceship.rect.centery -= 1.5
        spaceship.moving_up = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(game_settings, screen, spaceship)
        bullets.add(new_bullet)


def check_keyup_events(event, spaceship):
    if event.key == pygame.K_DOWN:
        spaceship.moving_down = False
    elif event.key == pygame.K_UP:
        spaceship.moving_up = False


def update_screen(game_settings, screen, spaceship, bullets):
    screen.fill(game_settings.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    game_settings = Settings()

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right > game_settings.windowWidth:
            bullets.remove(bullet)

# def fire_bullet(game_settings, screen, spaceship, bullets):
#
