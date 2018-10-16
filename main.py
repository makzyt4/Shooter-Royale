import pygame as pg
import pymunk as pm
import shooterroyale.physics as sr_p


def main():
    points = [None, None]

    space = pm.Space()
    space.gravity = (0, 1000)
    space.damping = 0.7

    pg.init()
    screen_size = (800, 600)
    display = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()

    rds = []
    sbs = []

    done = False

    while not done:
        for event in pg.event.get():
            mouse = pm.Vec2d(pg.mouse.get_pos())

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ragdoll = sr_p.Ragdoll(mouse)
                    ragdoll.load_elements()
                    ragdoll.add_to_space(space)
                    rds.append(ragdoll)
                elif event.button == 3:
                    points[0] = mouse
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 3:
                    points[1] = mouse
                    sb = sr_p.StaticBody((points[0] + points[1]) / 2,
                                         points[1] - points[0])
                    sb.load_elements()
                    sb.add_to_space(space)
                    sbs.append(sb)
                    points = [None, None]

            elif event.type == pg.MOUSEMOTION and points[0] is not None:
                points[1] = mouse
                rect = pg.Rect(points[0], points[1] - points[0])
                vertices = ((rect.left, rect.top),
                            (rect.left + rect.width, rect.top),
                            (rect.left + rect.width, rect.top + rect.height),
                            (rect.left, rect.top + rect.height),
                            (rect.left, rect.top))
                pg.draw.lines(display, (0, 128, 0), False, vertices)

            elif event.type == pg.QUIT:
                done = True

        display.fill((30, 30, 30))

        for rd in rds:
            rd.draw(display)
            rd.draw_wireframe(display)
        for sb in sbs:
            sb.draw_wireframe(display)

        pg.display.update()
        clock.tick(60)

        space.step(1/60)

    pg.quit()

if __name__ == '__main__':
    main()
