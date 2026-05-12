import pygame

from config import WIDTH, HEIGHT

pygame.init()

# 0. Подготовка игровых ресурсов
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def main():
    while True:

        # 1. Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Обновление состояния игры

        # 3. Отрисовка обновленного состояния игры
        screen.fill('white')
        pygame.display.update()
        pygame.time.delay(1000 // 60)

if __name__ == '__main__':
    main()
