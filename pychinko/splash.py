import pygame as pg
from state import State
from math import asin, pi
from tweener import *

class Splash(State):
    def __init__(self):
        super().__init__()
        self.running = True
        self.next = 'MAIN_MENU'
        self.time_active = 0
        self.title = self.font.render('^   PyChinko   ^', True, 'gold')
        self.subtitle = self.font.render('S o c o t r a ^ G a m e s', True, 'gold')
        self.title_rect = self.title.get_rect(midbottom=self.screen_rect.center)
        self.subtitle_rect = self.subtitle.get_rect(midtop=self.screen_rect.center)
        self.alpha = 255
        self.increment = -1
        self.veil = pg.Surface(self.screen.get_size())
        self.veil.fill((0,0,0))
        self.curtain = pg.Surface(self.screen.get_size())
        self.curtain.fill((0,0,0))
        self.curtain_rect = self.curtain.get_rect(center=self.screen_rect.center)
        self.curtain_rect.left = 300
        self.curtain_speed = 0
        self.smoothing = Tween(300.0, 1200.0, 3600, Easing.SINE, EasingMode.OUT,False,False,1)
        self.sfx = self.get_sfx('VICTORY')
        self.played = False

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 4000:
            self.running = False
        if self.time_active >= 3000:
            if not self.played:
                pg.mixer.Sound.play(self.sfx)
                self.played = True
        self.veil.set_alpha(self.alpha)
        if self.time_active >=500:
            self.smoothing.start()
            self.alpha += self.increment
            self.smoothing.update()
        if self.alpha <= 0 or self.alpha > 255:
            self.increment = -self.increment
            self.alpha += self.increment
        self.curtain_rect.left = int(self.smoothing.value)

    def draw(self):
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)        
        self.screen.blit(self.curtain, self.curtain_rect)
        self.screen.blit(self.veil, (0,0))

    