import pygame as pg
import pymunk as pm
import shooterroyale.physics as sr_p


def main():
    pg.init()
    screen_size = (800, 600)
    display = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        display.fill((30, 30, 30))

        pg.display.update()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()
