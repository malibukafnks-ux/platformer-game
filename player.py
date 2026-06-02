import pygame
from config import PLAYER_SPEED, GRAVITY, JUMP_POWER, WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_left = pygame.image.load('assets/player_left.png')
        self.image_left = pygame.transform.scale(self.image_left, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image_right = pygame.image.load('assets/player_right.png')
        self.image_right = pygame.transform.scale(self.image_right, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = self.image_right
        self.rect = self.image.get_rect(topleft=(x, y))

        self.velocity_y = 0
        self.on_ground = False
        self.lives = 3
        self.spawn_x = x
        self.spawn_y = y

    def reset_position(self):
        self.rect.topleft = (self.spawn_x, self.spawn_y)
        self.velocity_y = 0

    def update(self, platforms, level_width):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.image = self.image_left
        if keys[pygame.K_RIGHT]:
            self.image = self.image_right
            self.rect.x += PLAYER_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > level_width:
            self.rect.right = level_width

        prev_bottom = self.rect.bottom
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        self.on_ground = False
        for platform in pygame.sprite.spritecollide(self, platforms, False):
            if self.velocity_y > 0:
                if prev_bottom <= platform.rect.top + 4:
                    if self.rect.bottom >= platform.rect.top:
                        if platform.rect.left <= self.rect.centerx < platform.rect.right:
                            self.rect.bottom = platform.rect.top
                            self.velocity_y = 0
                            self.on_ground = True
                            break

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_POWER
