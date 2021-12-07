import pygame as pg
import sys

WIDTH = 520
HEIGHT = 360
BLACK = (0, 0, 0)


class Ball():
    def __init__(self, x, y, speed, x_, y_, surface, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.x_ = x_    # Направление движения
        self.y_ = y_
        self.s = surface
        self.r = radius

    def draw(self):
        pg.draw.circle(self.s, (255, 255, 255), (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_ * self.speed
        self.y_ += self.y_ * self.speed
        if self.x + self.r == WIDTH or self.x - self.r == 0:
            self.x_ = -self.x_

def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    mainS = pg.display.get_surface()
    FPS = 60
    clock = pg.time.Clock()
    ball = Ball(WIDTH / 2, HEIGHT / 2, 4, 1, 1, mainS, 20)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        mainS.fill(BLACK)
        ball.draw()
        ball.move()
        pg.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
