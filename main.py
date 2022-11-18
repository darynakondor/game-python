import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

screen = width, heigth = 800, 600

BALL_COLOR = 255, 255, 255
BACKGROUND_COLOR = 0, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(BALL_COLOR)
ball_rect = ball.get_rect()
ball_speed = 1

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working == False

    presed_keys = pygame.key.get_pressed()

    main_surface.fill(BACKGROUND_COLOR)

    main_surface.blit(ball, ball_rect)

    if presed_keys[K_DOWN]:
        ball_rect = ball_rect.move(0, ball_speed)

    if presed_keys[K_UP]:
        ball_rect = ball_rect.move(0, -ball_speed)

    if presed_keys[K_RIGHT]:
        ball_rect = ball_rect.move(ball_speed, 0)

    if presed_keys[K_LEFT]:
        ball_rect = ball_rect.move(-ball_speed, 0)

    pygame.display.flip()
