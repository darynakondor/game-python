import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random
from os import listdir

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

DARK_BLUE = 0, 0, 139

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)

IMAGES_PATH = 'goose_animation'

player_images = [pygame.image.load(
    IMAGES_PATH + '/' + file).convert_alpha() for file in listdir(IMAGES_PATH)]
player = player_images[0]
player_rect = player.get_rect()
player_speed = 10


def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_height = enemy.get_height()
    enemy_rect = pygame.Rect(
        width, random.randint(0, height - enemy_height), *enemy.get_size())
    enemy_speed = random.randint(4, 7)
    return [enemy, enemy_rect, enemy_speed]


def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_width = bonus.get_width()
    bonus_rect = pygame.Rect(
        random.randint(0, width - bonus_width), 0, *bonus.get_size())
    bonus_speed = random.randint(1, 3)
    return [bonus, bonus_rect, bonus_speed]


bg = pygame.transform.scale(pygame.image.load(
    'background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2800)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3200)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 125)

image_index = 0

scores = 0

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
        if event.type == CHANGE_IMAGE:
            image_index += 1
            if image_index == len(player_images):
                image_index = 0
            player = player_images[image_index]

    presed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True,
                      DARK_BLUE), (width - 30, 0))

    for enemy in enemies:
        main_surface.blit(enemy[0], enemy[1])
        enemy[1] = enemy[1].move(-enemy[2], 0)

        if enemy[1].left <= 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        main_surface.blit(bonus[0], bonus[1])
        bonus[1] = bonus[1].move(0, bonus[2])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))
        if player_rect.colliderect(bonus[1]):
            scores += 1
            bonuses.pop(bonuses.index(bonus))

    if presed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)

    if presed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)

    if presed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)

    if presed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move(-player_speed, 0)

    pygame.display.flip()
