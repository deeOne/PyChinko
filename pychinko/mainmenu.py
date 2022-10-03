import pygame as pg
from state import State

class MainMenu(State):
    def __init__(self):
        super().__init__()
        self.active_index = 0
        self.cooldown = 50
        self.time_active = 50
        self.options = {0:'Start', 1:'Exit'}
        self.next_options = {0:'OVERWORLD', 1:None}
        self.color_options = {0:'blue', 1:'white'}
        self.toggle = False
        self.toggle_sfx = self.get_sfx('ORB')
        self.select_sfx = self.get_sfx('SELECT')

    def update_text(self):
        self.start_button = self.font.render('New Game', True, 
                        self.color_options[self.active_index%2])
        self.start_button_rect = self.start_button.get_rect(midbottom=self.screen_rect.center)
        self.exit_button = self.font.render('Exit', True, 
                        self.color_options[1-self.active_index%2])
        self.exit_button_rect = self.start_button.get_rect(midtop=self.screen_rect.center)

    def get_next(self):
        return self.next_options[self.active_index%2]

    def get_event(self, e):
        if e.type == pg.K_ESCAPE:
            self.quit = True
        elif e.type == pg.KEYUP:
            if e.key == pg.K_UP or e.key == pg.K_DOWN:
                self.toggle = True
            elif e.key == pg.K_SPACE or e.key == pg.K_RETURN:
                pg.mixer.Sound.play(self.select_sfx)
                self.running = False

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= self.cooldown:
            if self.toggle:
                self.active_index += 1
                self.time_active = 0
                pg.mixer.Sound.play(self.toggle_sfx)
        self.toggle = False
        self.update_text()           

    def draw(self):
        self.screen.blit(self.start_button, self.start_button_rect)
        self.screen.blit(self.exit_button, self.exit_button_rect)