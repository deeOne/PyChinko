import pygame as pg
from commons import *

fonts = pg.font.get_fonts()

class State:
    def __init__(self):
        self.running = False
        self.quit = False
        self.exit = False
        self.next = None
        self.data = []
        self.persist = {}
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.font = pg.font.SysFont('jokerman', 48)

    def on_load(self, persistent):
        self.running = True
        self.persist = persistent

    def get_next(self):
        return self.next

    def get_persist(self):
        return self.persist
        
    def get_sfx(self, name):
        return pg.mixer.Sound(sfx_dict[name])

    def get_event(self, e):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def set_font(self, font):
        self.font = pg.font.SysFont(font, 48)

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((1200, 720))
    state = State()
    clock = pg.time.Clock()
    fps = 3
    frame = 0
    msg = state.font.render('test', True, 'gold')
    msg_rect = msg.get_rect(center=screen.get_rect().center)
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        screen.fill('black')
        state.set_font(fonts[frame])
        msg = state.font.render(fonts[frame], True, 'gold')
        screen.blit(msg, msg_rect)
        pg.display.update()
        clock.tick(fps)
        frame += 1
    pg.quit()




    
