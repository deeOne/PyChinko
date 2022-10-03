'''
Each level consists of a battlefield, pegboard, orb deck, and ui
On a 1200*720 screen with 24*24 tilesize, this looks like:

--------------------------------------------------
|               50x4 battlefield                 |
--------------------------------------------------
|  9   |                                         |
|  x   |                                         |
|  2   |              41x22                      |
|  2   |             pegboard                    |
|      |                                         |
| orb  |                                         |
| deck |                                         |
|      |-----------------------------------------|
|                   50x4 ui                      |
--------------------------------------------------
'''

import pygame as pg
from csv import reader
from commons import *
from state import State
from arrow import Arrow
from background import Background
from boundary import Boundary
from orb import Orb
from peg import Peg

class Level(State):
    def __init__(self, id='00'):
        super().__init__()        
        self.id = id
        self.next = 'GAME_OVER'
        self.map = self.load_map()
        self.assets = pg.sprite.Group()
        self.peg_group = pg.sprite.Group()
        self.ui_group = pg.sprite.Group()
        self.collision_group = pg.sprite.Group()

    def update_text(self, dt):
        self.fps_reader = self.font.render('FPS: '+str(1000//dt), True, 
                        'white')
        self.fps_reader_rect = self.fps_reader.get_rect(topleft=(0,0))
        self.dmg_reader = self.font.render('dmg: '+str(self.orb.damage), True, 
                        'white')
        self.dmg_reader_rect = self.fps_reader.get_rect(topleft=(0,48))


    def on_load(self, persistent):
        self.running = True
        self.persist = persistent
        self.load_assets()

    def on_exit(self):
        self.assets.empty()
        self.peg_group.empty()
        self.ui_group.empty()
        self.collision_group.empty()
        self.running = False

    def load_map(self):
        '''
        Each level will have some number of tilemap layers. This function
        finds each file, and returns a list of tuples corresponding to
        the map.
        '''
        map = {'background':[], 'boundary':[], 'peg':[]}
        for file in load_files('pychinko/map', self.id):
            with open(file) as f:
                rows = reader(f, delimiter=',')
                for row in rows:
                    for key,val in map.items():
                        if key in file:
                            val.append(list(row))
        print(map['background'])
        return map    

    def load_assets(self):
        for y, row in enumerate(self.map['background']):
            for x, col in enumerate(row):
                if col != '0':
                    Background(col, (x*TILE_WIDTH+X_OFFSET,y*TILE_HEIGHT+Y_OFFSET), 
                            [self.assets])
        for y, row in enumerate(self.map['boundary']):
            for x, col in enumerate(row):
                if col != '0':
                    Boundary(col, (x*TILE_WIDTH+X_OFFSET,y*TILE_HEIGHT+Y_OFFSET), 
                            [self.assets, self.collision_group])
        peg_num = 0
        for y, row in enumerate(self.map['peg']):
            for x, col in enumerate(row):
                if col != '0':
                    Peg(col, (x*TILE_WIDTH+X_OFFSET,y*TILE_HEIGHT+Y_OFFSET), peg_num,
                            [self.assets, self.peg_group, self.collision_group])
                    peg_num += 1

        self.orb = Orb('1', (648, 144), [self.assets, self.ui_group, self.collision_group])
        self.arrow = Arrow('2', (648, 168), [self.assets, self.ui_group])
        for peg in self.peg_group.sprites():
            if peg.num == 12: peg.modes['refresh'] = True

    def get_event(self, e):
        for ui in self.ui_group:
            ui.get_event(e)

    def update(self, dt):
        self.update_text(dt)
        self.ui_group.update()
        self.peg_group.update(dt)
        if self.arrow.shots_fired >= 4: 
            self.on_exit()

    def draw(self):
        self.assets.draw(self.screen)
        self.screen.blit(self.fps_reader, self.fps_reader_rect)
        self.screen.blit(self.dmg_reader, self.dmg_reader_rect)

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    level = Level('00')
    level.run()
    pg.quit()