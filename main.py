import sys, os
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
import pygame


from config import WIDTH, HEIGHT, FPS, TILE_SIZE, HITBOX_SHRINK, HURT_BOUNCE_POWER, GRAVITY
from level import Platform, LEVEL_1, load_level
from player import Player
from ui import draw_lives, draw_game_over, draw_win

pygame.init()

# 0. Подготовка игровых ресурсов
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jumper Max')
clock = pygame.time.Clock()
# platforms = pygame.sprite.Group()
# for x in range(0, WIDTH, TILE_SIZE):
#     platforms.add(Platform(x, HEIGHT - TILE_SIZE))



def shrunk_rect(sprite):
    return sprite.rect.inflate(-HITBOX_SHRINK, -HITBOX_SHRINK)


def player_touches(player, sprite):
    return shrunk_rect(player).colliderect(shrunk_rect(sprite))


def handle_falling(player):
    if player.rect.top > HEIGHT:
        player.lives -= 1
        player.reset_position()
        return True
    return False


def handle_traps(player, enemies, spikes):
    hit = any(player_touches(player, e) for e in enemies)
    hit = hit or any(player_touches(player, s) for s in spikes)
    if hit:
        player.lives -= 1
        player.velocity_y = HURT_BOUNCE_POWER
        player.on_ground = False
        return True
    return False
level_width = len(LEVEL_1[0]) * TILE_SIZE

def main():
    player = Player(50, 500)
    platforms,goal, spikes, enemies = load_level(LEVEL_1)
    game_over = False
    win = False
    hurt = False
    background = pygame.image.load('assets/background.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    while True:

        # 1. Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:

                    player.jump()
                if event.key == pygame.K_r and (game_over or win):
                    player = Player(50, 500)
                    platforms, goal, spikes, enemies = load_level(LEVEL_1)
                    game_over = False
                    win = False
                    hurt = False

        # 2. Обновление состояния игры
        #player.update(platforms)
        #enemies.update()
        if not game_over and not win:  # СТАЛО
            enemies.update()
            if hurt:
                player.velocity_y += GRAVITY
                player.rect.y += player.velocity_y
                if player.rect.top > HEIGHT:
                    if player.lives <= 0:
                        game_over = True
                    else:
                        player.reset_position()
                        hurt = False
            else:
                player.update(platforms, level_width)

                if handle_falling(player):
                    if player.lives <= 0:
                        game_over = True

                if not game_over and handle_traps(player, enemies, spikes):
                    hurt = True
                if goal is not None and player_touches(player, goal):
                    win = True
        # 3. Отрисовка обновленного состояния игры
        #screen.fill('white')
        # Камера следит за игроком
        camera_x = player.rect.centerx - WIDTH // 2
        if camera_x < 0:
            camera_x = 0
        if camera_x > level_width - WIDTH:
            camera_x = level_width - WIDTH

        # Фон повторяется
        bg_x = -(camera_x % WIDTH)
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + WIDTH, 0))

        # Все объекты рисуем со сдвигом камеры
        for sprite in platforms:
            screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y))

        for sprite in spikes:
            screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y))
        screen.blit(goal.image, (goal.rect.x - camera_x, goal.rect.y))
        player.draw(screen, camera_x)
        for sprite in enemies:
            screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y))
        draw_lives(screen, player.lives, 10, 10)
        if game_over:
            draw_game_over(screen, WIDTH, HEIGHT)
        if win:
            draw_win(screen, WIDTH, HEIGHT)
        pygame.display.update()
        clock.tick(FPS)



if __name__ == '__main__':
    main()
