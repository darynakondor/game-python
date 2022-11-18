import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

LIST_OF_BALL_COLORS = [(255, 255, 255), (255, 0, 0),
                       (60, 179, 113), (238, 130, 238), (0, 0, 255)]
BACKGROUND_COLOR = 0, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill((LIST_OF_BALL_COLORS[0]))
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working == False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.bottom >= heigth:
        ball.fill((LIST_OF_BALL_COLORS[1]))
    elif ball_rect.top <= 0:
        ball.fill((LIST_OF_BALL_COLORS[2]))
    elif ball_rect.right >= width:
        ball.fill((LIST_OF_BALL_COLORS[3]))
    elif ball_rect.left <= 0:
        ball.fill((LIST_OF_BALL_COLORS[4]))

    main_surface.fill((BACKGROUND_COLOR))

    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
