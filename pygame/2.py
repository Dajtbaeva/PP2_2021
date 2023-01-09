import pygame as pg

pg.init()
w, h = 800, 600
is_running = True
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
x, y = 0, 100
dx, dy = 5, 5
fps = 40

pg.display.set_caption('My game')
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()


while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill(white)

    font = pg.font.Font(None, 50)
    s = font.render("Dari", True, green)
    screen.blit(s, (w // 2, h // 2))

    font1 = pg.font.SysFont(None, 50)
    s1 = font.render("Abonti", True, green)
    screen.blit(s1, (30, 160))

    pg.display.flip()
pg.quit()