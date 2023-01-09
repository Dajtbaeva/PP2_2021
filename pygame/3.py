import pygame as pg
pg.init()

w, h, fps = 850, 650, 30

screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
running = True
x, y = w // 2, h // 2
speed = 20
r = 25
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()  
    if keys[pg.K_LEFT] and x - r > 0:
        x -= speed
    if keys[pg.K_RIGHT] and x + r < w:
        x += speed
    if keys[pg.K_DOWN] and y + r < h:
        y += speed
    if keys[pg.K_UP] and y - r > 0:
        y -= speed 
                
    screen.fill(WHITE)
    pg.draw.circle(screen, GREEN, (x, y), r)  
    pg.display.flip()
pg.quit()
