import pygame as pg
import random
import math

pg.init()
pg.display.set_caption("Trigonometry circle")
w, h, fps = 800, 600, 90
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
w1, h1 = w // 2 + 250, h // 2 

screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
running = True
x, y = w // 2 + 250, h // 2 
color = green
angle = 0
font = pg.font.SysFont('Georgia', 18)

while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        

    screen.fill(white)
    pg.draw.line(screen, black, (w // 2 + 250, h // 2), (w // 2 - 250, h // 2), 5)
    pg.draw.line(screen, black, (w // 2, h // 2 + 250), (w // 2, h // 2 - 250), 5)
    pg.draw.line(screen, red, (x, y), (w // 2, y), 3)
    pg.draw.line(screen, blue, (x, y), (x, h // 2), 3)


    pg.draw.circle(screen, black, (w // 2, h // 2), 250, 5)
    pg.draw.circle(screen, green, (x, y), 15)
    x = w // 2 + math.cos(math.radians(angle)) * 250
    y = h // 2 - math.sin(math.radians(angle)) * 250
    angle += 1

    text1 = f'sin{angle} = {math.sin(math.radians(angle % 360)):.2f}'
    text2 = f'cos{angle} = {math.cos(math.radians(angle % 360)):.2f}'
    r1 = font.render(text1, True, blue)
    r2 = font.render(text2, True, red)
    screen.blit(r1, (0, 0))
    screen.blit(r2, (0, 30))



    pg.display.flip()
pg.quit()

