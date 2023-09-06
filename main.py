import pygame as pg
from config import *

pg.init()

main_screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RE: Metal Warriors')

class Main:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.game_screen = pg.Surface((800, 600))
        self.fps = pg.time.Clock()

        self.playing = True
        self.main_start = True

    def run(self):
        while self.playing:
            if self.main_start:
                self.game_screen.fill('red')
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.main_start = False
                        self.playing = False
                    if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        self.main_start = False
                        self.playing = False
        
                self.main_screen.blit(self.game_screen, (0, 0))

            pg.display.update()
            self.fps.tick(60)

main = Main(main_screen)
main.run()
