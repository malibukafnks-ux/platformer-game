import pygame
from config import TILE_SIZE, ENEMY_PATROL_TILES
from traps import Spike, Enemy

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/goal.png')
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/tile.png')
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))


def load_level(level_data):
    goal = None
    platforms = pygame.sprite.Group()
    spikes = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    for row_index, row in enumerate(level_data):
        for col_index, symbol in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if symbol == '1':
                platforms.add(Platform(x, y))
            elif symbol == 'S':
                spikes.add(Spike(x, y + TILE_SIZE - 16))
            elif symbol == 'E':
                ground_row = level_data[row_index + 1] if row_index + 1 < len(level_data) else ''
                left_col = col_index
                for _ in range(ENEMY_PATROL_TILES):
                    if left_col > 0 and ground_row[left_col - 1] == '1':
                        left_col -= 1
                    else:
                        break
                right_col = col_index
                for _ in range(ENEMY_PATROL_TILES):
                    if right_col < len(row) - 1 and ground_row[right_col + 1] == '1':
                        right_col += 1
                    else:
                        break
                enemies.add(Enemy(x, y, left_col * TILE_SIZE, (right_col + 1) * TILE_SIZE))
            elif symbol == 'G':
                goal = Goal(x,y)
    return platforms,goal, spikes, enemies

LEVEL_1 = [
    '0000000000000000000000000',
    '0000000000000000000000000',
    '0000000000000000000000000',
    '0000000000000000000000000',
    '00000000000G0000000000000',
    '0000000000111000000000000',
    '0000000000000000000000000',
    '000000SE0000000000ES00000',
    '0000011110000000011110000',
    '0000000000000000000000000',
    '0000SS0000000000E00000000',
    '0000111100000001110000000',
    '0000000000000000000000000',
    '0000000000000000000000000',
    '0000000000111000000000000',
    '0000000000000000000000000',
    '0000000000000000000000000',
    '00000000000000000S0000000',
    '1111111111111111111111111',
]