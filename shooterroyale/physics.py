import pymunk as pm
import pygame as pg
import math


class Entity:
    def __init__(self):
        self._elements = []
        self._joints = []
        self.wireframe_color = (255, 0, 0)
        self.image = None
        self.shape_filter = pm.ShapeFilter(group=1)

    def add_element(self, position, size, mass, rect=None):
        body = pm.Body(mass)
        body.position = position
        body.moment = pm.moment_for_box(mass, size) * 5

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

        self._elements[-1][1].filter = pm.ShapeFilter(group=2)


class Ragdoll(Entity):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pg.image.load('./resources/player_m_rbody.png')

    def load_elements(self):
        self.add_element(self.position, (22, 20), 60.0, pg.Rect(58, 32, 30, 25))
        self.add_element(self.position + pm.Vec2d(0, -14), (12, 12), 4.0,
                         pg.Rect(58, 106, 12, 12))

        self.add_element(self.position + pm.Vec2d(-11, -8), (11, 7), 2.0,
                         pg.Rect(85, 20, 11, 7))
        self.add_element(self.position + pm.Vec2d(-19, -8), (14, 8), 2.0,
                         pg.Rect(71, 19, 14, 8))
        self.add_element(self.position + pm.Vec2d(-6, 14), (11, 12), 8.0,
                         pg.Rect(181, 64, 11, 12))
        self.add_element(self.position + pm.Vec2d(-5, 25), (11, 12), 4.0,
                         pg.Rect(181, 76, 11, 12))

        self.add_element(self.position + pm.Vec2d(11, -8), (11, 7), 2.0,
                         pg.Rect(160, 20, 11, 7))
        self.add_element(self.position + pm.Vec2d(19, -8), (14, 8), 2.0,
                         pg.Rect(171, 19, 14, 8))
        self.add_element(self.position + pm.Vec2d(6, 14), (11, 12), 8.0,
                         pg.Rect(64, 64, 11, 12))
        self.add_element(self.position + pm.Vec2d(5, 25), (11, 12), 4.0,
                         pg.Rect(64, 76, 11, 12))

        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[1][0],
                                     self.position + pm.Vec2d(0, -11)))
        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[1][0],
                                     self._elements[0][0].position +
                                     pm.Vec2d(0, -15)))

        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[2][0],
                                     self.position + pm.Vec2d(-10, -7)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[0][0],
                                           self._elements[2][0],
                                           math.radians(-90), math.radians(90)))

        self.add_joint(pm.PivotJoint(self._elements[2][0], self._elements[3][0],
                                     self.position + pm.Vec2d(-16, -11)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[2][0],
                                           self._elements[3][0],
                                           math.radians(0), math.radians(110)))

        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[4][0],
                                     self.position + pm.Vec2d(-5, 10)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[0][0],
                                           self._elements[4][0],
                                           math.radians(0), math.radians(90)))

        self.add_joint(pm.PivotJoint(self._elements[4][0], self._elements[5][0],
                                     self.position + pm.Vec2d(-4, 18)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[4][0],
                                           self._elements[5][0],
                                           math.radians(-110), math.radians(0)))

        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[6][0],
                                     self.position + pm.Vec2d(10, -7)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[0][0],
                                           self._elements[6][0],
                                           math.radians(-90), math.radians(90)))

        self.add_joint(pm.PivotJoint(self._elements[6][0], self._elements[7][0],
                                     self.position + pm.Vec2d(16, -8)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[6][0],
                                           self._elements[7][0],
                                           math.radians(-110), math.radians(0)))

        self.add_joint(pm.PivotJoint(self._elements[0][0], self._elements[8][0],
                                     self.position + pm.Vec2d(5, 10)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[0][0],
                                           self._elements[8][0],
                                           math.radians(-90), math.radians(0)))

        self.add_joint(pm.PivotJoint(self._elements[8][0], self._elements[9][0],
                                     self.position + pm.Vec2d(4, 18)))
        self.add_joint(pm.RotaryLimitJoint(self._elements[8][0],
                                           self._elements[9][0],
                                           math.radians(0), math.radians(110)))


class BulletBody(Entity):
    def __init__(self, position, velocity):
        super().__init__()
        self.velocity = velocity
        self.add_element(position, (3,3), 1.0, None)

    def load_elements(self):
        self._elements[-1][1].filter = pm.ShapeFilter(group=3)
        self._elements[-1][0].apply_force_at_local_point(self.velocity, (0, 0))
