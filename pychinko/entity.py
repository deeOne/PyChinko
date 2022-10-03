import pygame as pg
from commons import *

class Entity(pg.sprite.Sprite):
    def __init__(self, id, pos, groups) -> None:
        super().__init__(groups)
        self.id = id
        self.starting_pos = pos
        self.image = self.load_image(id)
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.starting_pos
        self.position = pg.math.Vector2(self.rect.center)
        self.velocity = pg.math.Vector2((0.0, 1.0))
        self.direction = self.velocity.normalize()
        self.modes = {}

    def add_modes(self, modes):
        for mode in modes:
            self.modes[mode] = False

    def get_active_modes(self):
        return tuple(self.modes.values())

    def toggle_mode(self, mode):
        self.modes[mode] = not self.modes[mode]

    def passive_mode(self):
        self.modes = dict.fromkeys(self.modes, False)

    def is_type(self,id):
        return id_dict[id] == self.id

    def get_sfx(self, name):
        return pg.mixer.Sound(sfx_dict[name])

    def load_image(self, id):
        return pg.image.load(image_dict[id]).convert()

    def distance_to(self, other):
        destination = pg.math.Vector2(other)
        return self.position.distance_to(destination)

    def on_reload(self):
        pass

    def on_hit(self):
        pass



