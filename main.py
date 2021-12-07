import pygame as pg

WIDTH = 360
HEIGHT = 480


class Ball():
    def __init__(self, x, y, speed, x_, y_):
        self.x = x
        self.y = y
        self.speed = speed
        self.x_ = x_    # Направление движения
        self.y_ = y_

    def draw(self):
        var = pg.draw

def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    mainS = pg.display.get_surface()
    FPS = 60
