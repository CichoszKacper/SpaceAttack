import sys

import pygame

from alien import Alien
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


def update_screen(game_settings, screen, spaceship, aliens, bullets):
    screen.fill(game_settings.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):
    game_settings = Settings()

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right > game_settings.windowWidth:
            bullets.remove(bullet)
def get_number_aliens_y (game_settings, alien_height):
    available_space_y = game_settings.windowHeight - 2 * alien_height
    number_aliens_y = int(available_space_y / (alien_height))

    return number_aliens_y

def create_alien (game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_height = alien.rect.height
    alien.y = alien_height + 2 * alien_height * alien_number
    alien.rect.y = alien.y
    alien.rect.x = game_settings.windowWidth - (alien.rect.width + 2 * alien.rect.width * row_number)
    aliens.add(alien)

def create_fleet (game_settings, screen, ship, aliens):

    alien = Alien(game_settings, screen)
    number_aliens_y = get_number_aliens_y(game_settings, alien.rect.height)

    number_rows = get_number_row(game_settings,ship.rect.width, alien.rect.width)
    for row_number in range (number_rows):
        for alien_number in range(number_aliens_y):
            create_alien(game_settings,screen,aliens,alien_number, row_number)

def get_number_row (game_settings, ship_width, alien_width):
    available_space_x = (game_settings.windowWidth - (3*alien_width) - ship_width)
    number_rows = int(available_space_x / (2*alien_width))
    return number_rows
