from types import DynamicClassAttribute
import pygame as pg

pg.init()
w, h = 800, 600
is_running = True
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
x, y = 100, 100
dx, dy = 5, 0
fps = 60


pg.display.set_caption('My game')
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()


while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill(white)

    pg.draw.rect(screen, black, (100, 100, 600, 400), 5)
    pg.draw.circle(screen, red, (x, y), 15)

    x += dx
    y += dy
    if x == 700 and y == 100:
        dx = 0
        dy = 5

    if x == 700 and y == 500:
        dx = -5
        dy = 0
     
    if x == 100 and y == 500:
        dx = 0
        dy = -5

    if x == 100 and y  == 100:
        dx = 5
        dy = 0
    

    pg.display.flip()
pg.quit()
