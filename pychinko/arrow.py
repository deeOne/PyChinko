import pygame as pg
import entity
import commons

class Arrow(entity.Entity):
    def __init__(self, id, pos, groups) -> None:
        super().__init__(id, pos, groups)
        self.id = '2'        
        self.starting_pos = pos
        self.ui_group = groups[1]
        self.add_modes(['aiming'])
        self.modes['aiming'] = True
        self.radius = commons.TILE_HEIGHT
        self.angle = 90.0
        self.rotation_speed = 2.0
        self.pole = pg.math.Vector2(self.position + (0, -self.radius))
        self.shots_fired = 1

    def rotate(self, dir=1):
        self.angle += dir*self.rotation_speed
        rot_vec = pg.Vector2()
        rot_vec.from_polar((self.radius, self.angle))
        self.position = self.pole + rot_vec
        self.rect.center = self.position

    def on_reload(self):
        self.position[0] = self.starting_pos[0]
        self.position[1] = self.starting_pos[1]
        self.rect.topleft = self.position
        self.angle = 90
        self.modes['aiming'] = True
        self.shots_fired += 1

    def get_event(self, e):
        if self.modes['aiming']:
            if e.type == pg.KEYUP:
                if e.key == pg.K_SPACE:
                    self.modes['aiming'] = False

    def update(self):
        if self.modes['aiming']:
            if pg.key.get_pressed()[pg.K_LEFT]:
                self.rotate()
            elif pg.key.get_pressed()[pg.K_RIGHT]:
                self.rotate(dir=-1)