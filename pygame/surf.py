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

surf1 = pg.Surface((300, 300)) # sizes
surf2 = pg.Surface((200, 200))
surf1.fill(red)
surf2.fill(green)

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill(white)
    screen.blit(surf1, (300, 200)) # coordinates
    pg.draw.circle(surf1, blue, (30, 30), 30)
    # surf1.blit(surf2, (0, 0))

    pg.display.flip()
pg.quit()
