'''
Probably don't need this at all, just use static images for background
'''

import pygame as pg
from entity import Entity

class Background(Entity):
    def __init__(self, id, pos, groups) -> None:
        super().__init__(id, pos, groups)

    def on_hit(self):
        pass

    def update(self):
        pass