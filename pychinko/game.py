import pygame as pg
from sys import exit
from commons import *
from splash import Splash
from mainmenu import MainMenu
from overworld import Overworld
from level import Level
from gameover import GameOver

class Game:
    def __init__(self, initial_state='SPLASH'):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.fill_color = FILL_COLOR
        self.fps = FPS
        self.clock = pg.time.Clock()
        self.dt = 0.01
        self.states = {'SPLASH':Splash(), 
                    'MAIN_MENU':MainMenu(),
                    'OVERWORLD':Overworld(),
                    'LEVEL':Level(), 
                    'GAME_OVER':GameOver(),
                    None:None
                    }
        self.state_id = initial_state
        self.state   = self.states[self.state_id]
        self.running = True

    def flip_state(self):
        self.state_id = self.state.get_next()
        persistent = self.state.get_persist()
        self.state = self.states[self.state_id]
        if not self.state:
            self.exit()
        self.state.on_load(persistent)

    def event_loop(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.exit()
            else:
                self.state.get_event(e)

    def update(self):
        if self.state.exit:
            self.exit()
        if not self.state.running:
            self.flip_state()
        self.state.update(self.dt)

    def draw(self):
        self.screen.fill(self.fill_color)
        self.state.draw()
        pg.display.update()

    def keep_time(self):
        self.dt = self.clock.tick(self.fps)

    def run(self):
        while self.running:
            self.event_loop()
            self.update()
            self.draw()
            self.keep_time()

    def exit(self):
        pg.quit()
        exit() 