'''
The main module that creates GameServer or GameClient object and run their loop.
'''
import pygame as pg
import shooterroyale.graphics as sr_g


def main():
    pg.init()
    screen_size = (800, 600)
    display = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()

    '''
    The main function that chooses between server and client version.
    '''
    sheet = sr_g.Sheet()
    sheet.load('./resources/player_m.png')

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        display.fill((30, 30, 30))

        display.blit(sheet.get_tile(3, 2), (0, 0))

        pg.display.update()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()
