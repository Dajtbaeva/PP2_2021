import pygame as pg
pg.init()
w, h = 800, 600
screen = pg.display.set_mode((w, h))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
is_running = True
clock = pg.time.Clock()
font = pg.font.SysFont("Times New Roman", 20, True)
finished = False
FPS = 15

rect1 = pg.Rect(100, 100, 50, 50)
rect2 = pg.Rect(300, 300, 50, 50)

# x, y, w, h

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill(white)
    pg.draw.rect(screen, blue, rect1)
    pg.draw.rect(screen, green, rect2)
    rect1.move_ip(1, 1)

    if rect1.colliderect(rect2):
        finished = True

    pg.display.flip()
pg.quit()
