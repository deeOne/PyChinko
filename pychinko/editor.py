#To be implemented next

import pygame as pg
from commons import *

class Map:
    def __init__(self, output_file='map/', 
                dimensions=(GRID_WIDTH, GRID_HEIGHT),keys=ids):
        self.output_file = output_file+'test.csv'
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.keys = keys
        self.grid = ['0']

        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('map editor')
        self.clock = pg.time.Clock()
        self.fps = 20

    def event_loop(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        pass    

if __name__ == '__main__':
    map = Map()
    map.run()
    map.exit()

