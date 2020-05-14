import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("transport.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0] / 7), int(self.image.get_rect().size[1] / 7)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.topright = self.screen_rect.topright

        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)