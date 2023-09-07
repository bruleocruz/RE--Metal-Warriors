import pygame as pg
from config import *
from game import Game
from editor import Editor

# Main Screen = Red
# Game Screen = Green
# Editor Screen = Blue

pg.init()

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RE: Metal Warriors')

class Main:
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        self.main_screen = pg.Surface((800, 600))
        self.fps = pg.time.Clock()

        self.game = Game(self)
        self.editor = Editor(self)

        self.playing = True
        self.main_start = True
        self.game_start = False
        self.editor_start = False

    def run(self):
        while self.playing:
            if self.main_start:
                self.main_screen.fill('red')
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.main_start = False
                        self.playing = False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.main_start = False
                            self.playing = False
                        elif event.key == pg.K_g:  # Game Transition;
                            self.game_start = True
                            self.main_start = False
                        elif event.key == pg.K_e:
                            self.editor_start = True
                            self.main_start = False
                self.SCREEN.blit(self.main_screen, (0, 0))
            
            if self.game_start:
                self.game.run()
            
            if self.editor_start:
                self.editor.run()

            pg.display.update()
            self.fps.tick(60)

main = Main(SCREEN)
main.run()
