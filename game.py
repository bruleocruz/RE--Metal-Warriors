import pygame as pg

class Game:
    def __init__(self, main):
        self.SCREEN = main.SCREEN
        self.main = main
        self.game_screen = pg.Surface((800, 600))

    def game_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:  # Main Transition;
                    self.main.main_start = True
                    self.main.game_start = False
                elif event.key == pg.K_e:  # Editor Transition;
                    self.main.editor_start = True
                    self.main.game_start = False
                elif event.key == pg.K_ESCAPE:
                    self.main.playing = False

    def run(self):
        self.game_screen.fill('Green')
        self.game_events()
        self.SCREEN.blit(self.game_screen, (0, 0))
