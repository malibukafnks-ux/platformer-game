import math
import pygame
def draw_lives(screen, lives, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(text, (x, y))
def _draw_pulsing_message(screen, width, height, message, overlay_color, text_color, shadow_color):
    ticks = pygame.time.get_ticks()
    pulse = (math.sin(ticks* 0.01) + 1) / 2
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    r, g, b = overlay_color
    overlay.fill((r, g, b, 70 + int(50* pulse)))
    screen.blit(overlay, (0, 0))
    font = pygame.font.Font(None, 70 + int(10* pulse))
    wobble_y = int(math.sin(ticks* 0.008) * 8)
    text = font.render(message, True, text_color)
    rect = text.get_rect(center=(width // 2, height // 2 + wobble_y))
    shadow = font.render(message, True, shadow_color)
    shadow_rect = shadow.get_rect(center=(rect.centerx + 4, rect.centery + 4))
    screen.blit(shadow, shadow_rect)
    screen.blit(text, rect)
def draw_game_over(screen, width, height):
    _draw_pulsing_message(screen, width, height, 'GAME OVER', (90, 0, 0), (255, 60, 20), (40, 0, 0))
def draw_win(screen, width, height):
    _draw_pulsing_message(screen, width, height, 'YOU WIN!', (0, 90, 0), (20, 220, 20), (0, 40, 0))