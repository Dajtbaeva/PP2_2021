import pygame as pg
import random
pg.init()
w, h = 800, 600
screen = pg.display.set_mode((w, h))
pg.display.set_caption("Ping Pong by DreamTeam")
color = (94, 147, 75)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
is_running = True
clock = pg.time.Clock()
font = pg.font.SysFont("Times New Roman", 20, True)
ball = (0, 0, 0)
c1, c2 = w // 2, h // 2
dc1, dc2 = 5, -5
r = 20
r1, r2 = 50, h // 2 - 100
r3, r4 = 750, h // 2 - 100
score1, score2 = 0, 0
lose = False
FPS = 50

while is_running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.fill((255, 255, 255))
    pg.draw.circle(screen, ball, (c1, c2), 20)
    pg.draw.rect(screen, red, (r1, r2, 10, 200))
    pg.draw.rect(screen, blue, (r3, r4, 10, 200))

    if r2 + 200 >= 600:
        r2 = 600 - 200
    if r2 <= 0:
        r2 = 0
    if r4 + 200 >= 600:
        r4 = 600 - 200
    if r4 <= 0:
        r4 = 0

    ball_point = (c1, c2)
    if ball_point[0] == w:
        score1 += 1
        lose = True
    if ball_point[0] == 0:
        score2 += 1
        lose = True

    if c2 + r >= h or c2 - r <= 0:
        dc2 *= -1
    c1 += dc1
    c2 += dc2

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        r4 -= 7
    elif keys[pg.K_DOWN]:
        r4 += 7
    if keys[pg.K_w]:
        r2 -= 7
    elif keys[pg.K_s]:
        r2 += 7

    ball_point = (c1, c2)
    if (ball_point[1] in range(r4, r4 + 200) and ball_point[0] == r3 - r):
        dc1 *= -1
        dc2 *= -1
    if (ball_point[1] in range(r2, r2 + 200) and ball_point[0] == r1 + r):
        dc1 *= -1
        dc2 *= -1

    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False
            if event.type == pg.KEYDOWN:
                c1, c2 = w // 2, h // 2
                lose = False
                running = True
        pg.draw.rect(screen, color, (w // 2 - 100, h // 2 - 100, 200, 200))
        if score1 > score2:
            text = font.render(f"Winner is #1", True, white)
            text2 = font.render(f"Current score is {score1}", True, white)
            screen.blit(text, (w//2 - 70, h //2) )
            screen.blit(text2,(w//2 - 70, h//2 - 20))
            score1, score2 = 0, 0
        else:
            text = font.render(f"Winner is #2", True, white)
            text2 = font.render(f"Current score is  {score2}", True, white)
            screen.blit(text, (w//2 - 70, h //2) )
            screen.blit(text2,(w//2 - 70, h//2 - 20))
            score1, score2 = 0, 0

        # screen.blit(text, (w//2 - 70, h //2) )
        # screen.blit(text2,(w//2 - 70, h//2 - 20))
        pg.display.flip()

    pg.display.flip()
pg.quit()
