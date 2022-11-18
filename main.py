import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

BALL_COLOR = 255, 255, 255
BACKGROUND_COLOR = 0, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill((BALL_COLOR))
ball_rect = ball.get_rect()

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working == False

    main_surface.fill((BACKGROUND_COLOR))

    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
