import pygame as pg
import random

pg.init()
pg.display.set_caption("Ball moving")
w, h, fps = 800, 600, 90
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
running = True
x, y = 350, 150
color = green
dx, dy = 0, 0
speed = 1
while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                dx = speed
                dy = 0
            if event.key == pg.K_LEFT:
                dx = -speed
                dy = 0
            if event.key == pg.K_DOWN:
                dx = 0
                dy = speed
            if event.key == pg.K_UP:
                dx = 0
                dy = -speed
            if event.key == pg.K_SPACE:
                speed += 1
                if dx == 0:
                    dy = speed
                else:
                    dx = speed
        
    screen.fill(white)
    pg.draw.ellipse(screen, color, (x % w, y % h, 50, 60))
    x += dx
    y += dy
    pg.display.flip()
pg.quit()

