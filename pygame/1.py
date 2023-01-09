import pygame as pg
from datetime import datetime 
import math
pg.init()
w, h, fps = 800, 600, 60
is_running = True
pg.display.set_caption('Mickey Clock')
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()

ww, hh = w // 2, h // 2 # initial coordinates
r = hh - 75 # size of clock lines
r_list = {'sec': r - 10, 'min': r - 55, 'hour': r - 100}

background_img = pg.image.load("./images/mickeyclock.jpg")
background_img = pg.transform.scale(background_img, (w, h))
right_hand = pg.image.load("./images/right_hand.png").convert_alpha()
right_hand = pg.transform.scale(right_hand, (180, 100))
left_hand = pg.image.load("./images/left_hand.png").convert_alpha()
left_hand = pg.transform.scale(left_hand, (120, 100))
rect1 = right_hand.get_rect(bottomleft = (ww, hh))
rect2 = left_hand.get_rect(bottomright = (ww, hh))

def get_clock_pos(clock_dict, clock_hand, key):
    x = ww + r_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = hh + r_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

font = pg.font.SysFont('Verdana', 25)
clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill('white')
    screen.blit(background_img, (0, 0))
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    # 10:14:49 === 10 % 12 -> 10 * 5 = 50 -> 50 + 14 // 12 = 51 -> 51 % 60 = 51
    # 15:15:34 === 15 % 15 -> 3 * 5 = 15 -> 15 + 15 // 12 = 16 -> 16 % 60 = 16

    pg.draw.line(screen,'red', (ww, hh), get_clock_pos(clock60, hour, 'hour'), 13)
    pg.draw.line(screen,'green', (ww, hh), get_clock_pos(clock60, minute, 'min'), 8)
    pg.draw.line(screen,'black', (ww, hh), get_clock_pos(clock60, second, 'sec'), 4)
    pg.draw.circle(screen,'white', (ww, hh), 8)

    time_text = font.render(f'{t:%H:%M:%S}', True, 'white', 'red')
    screen.blit(time_text, (25, 25))
    screen.blit(right_hand, rect1)
    screen.blit(left_hand, rect2)
    rect1.move_ip(get_clock_pos(clock60, second, 'sec'))
    pg.display.flip()
pg.quit()