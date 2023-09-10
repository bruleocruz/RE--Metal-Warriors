import pygame as pg
from config import *

class Editor:
    def __init__(self, main):
        self.SCREEN = main.SCREEN
        self.main = main
        self.editor_screen = pg.Surface((800, 600))
    
    def editor_events(self):
         for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:  # Main Transition;
                        self.main.main_start = True
                        self.main.editor_start = False
                    elif event.key == pg.K_g:  # Game Transition;
                         self.main.game_start = True
                         self.main.editor_start = False
                    elif event.key == pg.K_ESCAPE:
                         self.main.playing = False
    
    def run(self):
        self.editor_screen.fill('Blue')
        self.editor_events()
        self.SCREEN.blit(self.editor_screen, (0, 0))
