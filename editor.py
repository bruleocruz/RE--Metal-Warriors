import pygame as pg
from config import *
from tiles import Tile


class Editor:
    def __init__(self, main, map):
        self.SCREEN = main.SCREEN
        self.main = main
        self.map = map
        self.tiles = pg.sprite.Group()
        self.editor_screen = pg.Surface((800, 600))
        self.editor_screen.fill((0, 255, 255))

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

    def draw_lines(self):
        for vertical in range(0, int(WIDTH / TILE_SET + 1)):
            result = vertical * TILE_SET
            pg.draw.line(self.editor_screen,
                         'black',
                         (result, 0),
                         (result, HEIGHT))

        for horizontal in range(0, int(HEIGHT / TILE_SET + 1)):
            result = horizontal * TILE_SET
            pg.draw.line(self.editor_screen,
                         'black',
                         (0, result),
                         (WIDTH, result))

    def run(self):
        self.editor_events()
        self.draw_lines()
        self.SCREEN.blit(self.editor_screen, (0, 0))
        pg.display.update()
