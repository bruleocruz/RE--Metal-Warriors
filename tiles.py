import pygame as pg
from config import *

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((TILE_SET, TILE_SET))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x_scroll = 0
        self.y_scroll = 0

    def update(self):
        self.rect.x += self.x_scroll
        self.rect.y += self.y_scroll
