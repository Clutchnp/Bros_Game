import pygame as pg
from pygame.locals import *


def main():
    exit = False
    while not exit:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit = True

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    exit = True

        pg.time.Clock().tick(60)

        draw_grid()

        pg.display.update()


def get_grid_info():
    block_size = h // 10

    offset_x = -block_size
    offset_y = -3 * block_size

    center = (w // 2 + offset_x, h // 2 + offset_y)

    return block_size, center


def draw_grid():
    block_size, center = get_grid_info()

    pg.draw.circle(win, "red", (w // 2, h // 2), 10)

    for x in range(center[0], center[0] + (7 * block_size), block_size):
        for y in range(center[1], center[1] + (6 * block_size), block_size):
            rect = pg.Rect(x, y, block_size, block_size)
            pg.draw.rect(win, "white", rect, 1)


if __name__ == "__main__":
    pg.init()

    h = 1080
    w = 1980

    win = pg.display.set_mode((w, h), pg.FULLSCREEN)
    pg.display.set_caption("Pygame Test")

    w, h = pg.display.get_surface().get_width(), pg.display.get_surface().get_height()

    main()
