import pygame as pg
import random

pg.init()
pg.display.set_caption("Square moving")
w, h, fps = 800, 600, 90
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
running = True

rec_x, rec_y = 70, 70
dx, dy = 3, 3
x, y = 300, 150
color = green
screen.fill(white)

while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pg.draw.rect(screen, color, (x, y, rec_x, rec_y))
    x += dx
    y += dy

    if x >= w - rec_x or x <= 0:
        dx *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if y >= h - rec_y or y <= 0:
        dy *= -1
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pg.display.flip()
pg.quit()

