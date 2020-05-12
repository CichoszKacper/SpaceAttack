import pygame

from settings import Settings


class Ship():
    def __init__(self, game_settings, screen):
        # Starting position
        self.screen = screen
        self.game_settings = game_settings


        # Load ship image
        self.image = pygame.image.load("Spaceship.png")
        self.image = pygame.transform.flip(self.image,True,False)
        # Change size of the spaceship
        self.image = pygame.transform.scale(self.image,(int(self.image.get_rect().size[0]/4),int(self.image.get_rect().size[1]/4)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start new ship at left side of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centery)

        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.game_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.center -= self.game_settings.ship_speed_factor

        self.rect.centery = self.center

    def blitme(self):
        # Draw ship at current location
        self.screen.blit(self.image,self.rect)