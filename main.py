import pygame

from config import WIDTH, HEIGHT, FPS, TILE_SIZE
from level import Platform, LEVEL_1, load_level
from player import Player

pygame.init()

# 0. Подготовка игровых ресурсов
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jumper Max')
clock = pygame.time.Clock()
# platforms = pygame.sprite.Group()
# for x in range(0, WIDTH, TILE_SIZE):
#     platforms.add(Platform(x, HEIGHT - TILE_SIZE))
platforms,spikes,enemies = load_level(LEVEL_1)

def main():
    player = Player(50, 500)
    while True:

        # 1. Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    player.jump()

        # 2. Обновление состояния игры
        player.update(platforms)
        enemies.update()
        # 3. Отрисовка обновленного состояния игры
        screen.fill('white')
        platforms.draw(screen)
        spikes.draw(screen)
        screen.blit(player.image, player.rect)
        enemies.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
