import pygame as pg
from datetime import datetime 
pg.init()

w, h, fps = 800, 600, 60
is_running = True

pg.display.set_caption('Clock')
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
font = pg.font.SysFont('Verdana', 25)

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill('white')
    
    t = datetime.now()
    time_text = font.render(f'{t:%H:%M:%S}', True, 'red', 'green')
    screen.blit(time_text, (25, 25))
    pg.display.flip()
pg.quit()