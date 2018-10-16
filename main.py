import pygame as pg
import pymunk as pm
import shooterroyale.physics as sr_p


def main():
    points = [None, None]

    space = pm.Space()
    space.gravity = (0, 0)
    #space.damping = 0.01

    pg.init()
    screen_size = (800, 600)
    display = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()

    rds = []
    sbs = []
    bts = []
    phantom_rect = None

    done = False
    gravity = False
    wireframe = False

    while not done:
        if gravity:
            space.gravity = (0, 1000)
        else:
            space.gravity = (0, 0)

        for event in pg.event.get():
            mouse = pm.Vec2d(pg.mouse.get_pos())

            if event.type == pg.MOUSEMOTION and points[0] is not None:
                points[1] = mouse
                phantom_rect = pg.Rect(points[0], points[1] - points[0])
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ragdoll = sr_p.Ragdoll(mouse)
                    ragdoll.load_elements()
                    ragdoll.add_to_space(space)
                    rds.append(ragdoll)
                elif event.button == 2:
                    bullet = sr_p.BulletBody(mouse, (-100000, -100000))
                    bullet.load_elements()
                    bullet.add_to_space(space)
                    bts.append(bullet)
                elif event.button == 3 and points[0] is None:
                    points[0] = mouse
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 3:
                    points[1] = mouse
                    sb = sr_p.StaticBody((points[0] + points[1]) / 2,
                                         points[1] - points[0])
                    sb.load_elements()
                    sb.add_to_space(space)
                    sbs.append(sb)
                phantom_rect = None
                points = [None, None]
            elif event.type == pg.KEYDOWN:
                if event.key == ord('g'):
                    gravity ^= True
                elif event.key == ord('w'):
                    wireframe ^= True
            elif event.type == pg.QUIT:
                done = True

        display.fill((30, 30, 30))

        for rd in rds:
            rd.draw(display)
            if wireframe:
                rd.draw_wireframe(display)
        for sb in sbs:
            sb.draw_wireframe(display)
        for bt in bts:
            bt.draw_wireframe(display)

        if phantom_rect is not None:
            x, y, w, h = (phantom_rect.left, phantom_rect.top,
                          phantom_rect.width, phantom_rect.height)
            vertices = (pm.Vec2d(x, y),
                        pm.Vec2d(x + w, y),
                        pm.Vec2d(x + w, y + h),
                        pm.Vec2d(x, y + h))
            pg.draw.lines(display, (0, 255, 0), True, vertices)

        pg.display.update()
        clock.tick(60)

        space.step(1/60)

    pg.quit()

if __name__ == '__main__':
    main()
