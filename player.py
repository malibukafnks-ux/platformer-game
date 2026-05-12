import pygame
from config import PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 48))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=(x, y))