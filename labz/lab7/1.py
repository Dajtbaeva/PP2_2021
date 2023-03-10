import pygame as pg
from datetime import datetime
pg.init()

w, h = 800, 600
is_running = True
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Mickey Clock')
clock = pg.time.Clock()

pg.mixer.init()
pg.mixer.music.load("./sound/background.mp3")
pg.mixer.music.play(-1)

def convert(time):
    return 360 - time * 6

def rotation(surf, image, topleft, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

font = pg.font.SysFont('Arial', 25)
background = pg.image.load('./images/mickeyclock.jpg')
background = pg.transform.scale(background,(w, h))
hand1 = pg.image.load('./images/left_hand.png').convert_alpha()
hand2 = pg.image.load('./images/right_hand.png').convert_alpha()

while is_running:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill('white')
    screen.blit(background, (0, 0))
    t = datetime.now()

    textt = font.render(f'{t:%H:%M:%S}', True, 'black', 'white')
    minute, second = t.minute, t.second
    screen.blit(textt,(10, 10))

    angle1 = convert(t.second + 1)
    angle2 = convert(t.minute)
    rotation(screen, hand1, (255,150), angle1)
    rotation(screen, hand2, (255, 150), angle2 - 3)
    pg.display.flip()
pg.quit()
