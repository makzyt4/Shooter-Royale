import pymunk as pm
import pygame as pg
import math


class Entity:
    def __init__(self):
        self._elements = []
        self._joints = []
        self.wireframe_color = (255, 0, 0)
        self.image = None
        self.shape_filter = pm.ShapeFilter(group=0)

    def add_element(self, position, size, mass, rect=None):
        body = pm.Body(mass)
        body.position = position
        body.moment = pm.moment_for_box(mass, size) * 5
        print(body.moment)

        if rect is None:
            img = None
        else:
            img = self.image.subsurface(rect)

        shape = pm.Poly.create_box(body, size)
        shape.friction = 15.0
        shape.filter = self.shape_filter

        self._elements.append([body, shape, size, mass, img])

    def add_joint(self, joint):
        self._joints.append(joint)

    def add_to_space(self, space):
        for elem in self._elements:
            print(*elem[:2])
            space.add(*elem[:2])
        space.add(*self._joints)

    def draw_wireframe(self, surface):
        for elem in self._elements:
            body = elem[0]
            position = body.position
            shape = elem[1]
            points = shape.get_vertices()

            points.append(points[0])
            points = [p.rotated(body.angle) + position for p in points]

            pg.draw.lines(surface, self.wireframe_color, False, points)

    def draw(self, surface):
        for elem in self._elements:
            if elem[4] is None:
                return

            pos = elem[0].position

            img = pg.transform.rotate(elem[4], -math.degrees(elem[0].angle))
            offset = pm.Vec2d(img.get_size()) / 2
            print(offset)
            pos -= offset
            surface.blit(img, (pos[0], pos[1]))


class StaticBody(Entity):
    def __init__(self, position, size):
        super().__init__()
        self.wireframe_color = (0, 255, 0)
        self.position = position
        self.size = size

    def load_elements(self):
        self.add_element(self.position, self.size, 100.0)
        self._elements[-1][0].body_type = pm.Body.STATIC


class Ragdoll(Entity):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pg.image.load('./resources/player_m_rbody.png')

    def load_elements(self):
        self.add_element(self.position, (22, 20), 60.0, pg.Rect(62, 32, 22, 20))
