import pygame

from config import WIDTH, HEIGHT, FPS
from player import Player

pygame.init()

# 0. Подготовка игровых ресурсов
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jumper Max')
clock = pygame.time.Clock()

def main():
    player = Player(50, 500)
    while True:

        # 1. Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Обновление состояния игры

        # 3. Отрисовка обновленного состояния игры
        screen.fill('white')
        screen.blit(player.image, player.rect)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
