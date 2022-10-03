import pygame as pg
from random import randint
from entity import Entity

class Peg(Entity):
    def __init__(self, id, pos, num, groups):
        super().__init__(id, pos, groups)
        self.id = '5'
        self.num = num
        print(self.num)
        self.peg_group = groups[1]
        self.collision_group = groups[2]
        self.radius = 12
        self.add_modes(['vanish', 'refresh', 'refreshed'])
        self.copy = self.image.copy()
        self.vanish_color = pg.Color(132, 23, 213, 255)
        self.hit_sfx = [self.get_sfx('PEG_0'), 
                        self.get_sfx('PEG_1'),
                        self.get_sfx('PEG_2'),
                        self.get_sfx('PEG_3')
        ]
        self.refresh_sfx = self.get_sfx('REFRESH')

    def on_hit(self):
        if self.modes['refresh']:
            self.modes['refreshed'] = True
            pg.mixer.Sound.play(self.refresh_sfx)
        else:
            self.modes['vanish'] = True
            pg.mixer.Sound.play(self.hit_sfx[randint(0,3)])

    def on_reload(self):
        pass

    def update(self, dt):
        #restore all pegs and select new refresh if refreshed
        if self.modes['refreshed']:
            self.modes['refresh'] = False
            self.image = self.copy
            self.modes['refreshed'] = False
            self.modes['vanish'] = False
            next_refresh = randint(0, len(self.peg_group)-1)
            for peg in self.peg_group:
                if peg.num == next_refresh:
                    peg.image = peg.load_image('6')
                    peg.modes['refresh'] = True
                    continue
                if peg.modes['vanish']:
                    peg.image = peg.copy
                peg.modes['vanish'] = False

        #hide all hit pegs
        elif self.modes['vanish']:
            self.image.fill(self.vanish_color)
            self.image.set_colorkey(self.vanish_color)

        #draw refresh peg
        elif self.modes['refresh']:
            self.image = self.load_image('6')
            self.image.set_colorkey('white')


        
