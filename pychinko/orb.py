import pygame as pg
from entity import Entity
import math
from commons import *

class Orb(Entity):
    def __init__(self, id, pos, groups) -> None:
        super().__init__(id, pos, groups)
        self.id = '1'
        self.assets = groups[0]
        self.ui_group = groups[1]
        self.collision_group = groups[2]
        self.add_modes(['active', 'aiming'])
        self.modes['active'] = True
        self.radius = 12
        self.velocity = pg.math.Vector2((0.0, 7.0))
        self.initial_velocity = self.velocity.copy()
        self.direction = self.velocity.normalize()
        self.acceleration = 0.22
        self.max_velocity = 18.0
        self.damage = 0

    def bounce(self, other):
        difference = self.position - other
        normal = difference.normalize()
        angle = normal.angle_to(self.direction)

        self.direction[0] = normal[0]+self.direction[0]*abs(math.cos(math.radians(angle)))
        self.direction[1] = normal[1]+self.direction[1]*abs(math.sin(math.radians(angle)))
        self.direction = self.direction.normalize()
        self.velocity = self.velocity.magnitude()*self.direction

    def check_collision(self):
        if self.position[0] < X_OFFSET+TILE_WIDTH or self.position[0] > SCREEN_WIDTH-TILE_WIDTH:
            self.position[0] -= self.velocity[0]
            self.direction[0] = -self.direction[0]
            self.velocity[0] = -self.velocity[0]
            self.on_hit('WALL')
        if self.position[1] < Y_OFFSET+TILE_WIDTH:
            self.position[1] -= self.velocity[1]
            self.direction[1] = -self.direction[1]
            self.velocity[1] = -self.velocity[1]
            self.on_hit('CEILING')
        for sprite in self.collision_group:
            if sprite.is_type('PEG'):
                if sprite.modes['vanish'] == False:
                    if pg.sprite.collide_circle(self, sprite):
                        self.bounce(sprite.position)
                        sprite.on_hit()
                        self.on_hit('PEG')

    def on_hit(self, id):
        match id:
            case 'PEG':
                self.damage += 2
            case 'WALL' | 'CEILING':
                pass
            case _:
                pass

    def on_reload(self):
        print('damage to enemy: ', self.damage)
        self.damage = 0
        self.rect.topleft = self.starting_pos
        self.position = self.rect.center
        self.velocity = self.initial_velocity
        self.direction = self.velocity.normalize()
        self.modes['active'] = True

    def get_event(self, e):
        if self.modes['active']:
            if e.type == pg.KEYUP:
                if e.key in {pg.K_LEFT, pg.K_RIGHT}:
                    self.modes['aiming'] = True
                elif e.key == pg.K_SPACE:
                    self.modes['active'] = False
                    self.modes['aiming'] = False

    def update(self):
        if not self.modes['active']:
            speed = self.velocity.magnitude()
            self.check_collision()
            if speed > self.max_velocity:
                self.velocity = self.direction*self.max_velocity
            else:
                self.velocity = speed*self.direction
            self.velocity[1]+=self.acceleration
            self.position += self.velocity
            self.direction = self.velocity.normalize()

            self.rect.center = self.position
            if self.rect.bottom > SCREEN_HEIGHT:
                for sprite in self.assets:
                    sprite.on_reload()  

        elif self.modes['aiming']:            
            for sprite in self.ui_group:
                if sprite.is_type('ARROW'):
                    vec = sprite.position - self.position
                    self.direction = vec.normalize()
