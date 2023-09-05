import pygame as pg
from config import *

pg.init()

main_screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RE: Metal Warriors')

playing = True

while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            playing = False
    
    pg.display.update()
