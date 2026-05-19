import pygame

from config import TILE_SIZE


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, 16))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left_bound, right_bound):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.left_bound = left_bound
        self.right_bound = right_bound

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.left_bound or self.rect.right >= self.right_bound:
            self.speed *= -1
