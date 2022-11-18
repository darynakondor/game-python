import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

BALL_COLOR = 255, 255, 255
ENEMY_COLOR = 255, 0, 0
BONUS_COLOR = 240, 230, 140
BACKGROUND_COLOR = 0, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(BALL_COLOR)
ball_rect = ball.get_rect()
ball_speed = 5


def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(ENEMY_COLOR)
    enemy_rect = pygame.Rect(
        width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(BONUS_COLOR)
    bonus_rect = pygame.Rect(
        random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 4)
    return [bonus, bonus_rect, bonus_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 1500)

enemies = []
bonuses = []

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working == False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    presed_keys = pygame.key.get_pressed()

    main_surface.fill(BACKGROUND_COLOR)

    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        main_surface.blit(enemy[0], enemy[1])
        enemy[1] = enemy[1].move(-enemy[2], 0)

        if enemy[1].left <= 0 or ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        main_surface.blit(bonus[0], bonus[1])
        bonus[1] = bonus[1].move(0, bonus[2])

        if bonus[1].bottom >= height or ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))

    if presed_keys[K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move(0, ball_speed)

    if presed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)

    if presed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)

    if presed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    pygame.display.flip()
