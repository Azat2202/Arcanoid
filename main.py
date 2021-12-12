import pygame as pg
import pygame.freetype
import sys
from random import uniform
from settings import *


def buttons_handler(platformL, platformR):
    pressed_buttons = pg.key.get_pressed()
    if pressed_buttons[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()
    if pressed_buttons[pg.K_w]:
        platformL = platformL.move(0, -move_value)
    if pressed_buttons[pg.K_s]:
        platformL = platformL.move(0, move_value)
    if pressed_buttons[pg.K_UP]:
        platformR = platformR.move(0, -move_value)
    if pressed_buttons[pg.K_DOWN]:
        platformR = platformR.move(0, move_value)
    return platformL, platformR


def draw_dots_line(x, y, delta, Surface):
    for y_ in range(0, y, delta * 2):
        pg.draw.line(Surface, WHITE, (x, y_), (x, y_ + delta), 3)


def main():
    pg.init()
    pg.display.set_mode((0, 0), pygame.FULLSCREEN)
    mainS = pg.display.get_surface()
    clock = pg.time.Clock()
    xB, yB = HALF_WIDTH, HALF_HEIGHT
    platformL = pygame.Rect(X_OFFSET, HALF_HEIGHT, 10, 50)
    platformR = pygame.Rect(WIDTH - X_OFFSET, HALF_HEIGHT, 10, 50)
    x_, y_ = 1, 1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        platformL, platformR = buttons_handler(platformL, platformR)
        mainS.fill(BLACK)
        draw_dots_line(HALF_WIDTH, HEIGHT, 10, mainS)
        circle = pg.draw.circle(mainS, WHITE, (xB, yB), 10)
        if circle.top >= HEIGHT or circle.bottom <= 0:
            y_ *= -1
        if circle.right >= platformR.left and platformR.top <= circle.center[1] <= platformR.bottom:
            x_ *= -1
        elif circle.left <= platformL.right and platformL.top <= circle.center[1] <= platformL.bottom:
            x_ *= -1
        xB += x_ * speed
        yB += y_ * speed
        pg.draw.rect(mainS, WHITE, rect=platformL)
        pg.draw.rect(mainS, WHITE, rect=platformR)
        if circle.left < 0 or circle.right > WIDTH:
            print('GAME OVER')
            pg.quit()
            sys.exit()
        pg.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
