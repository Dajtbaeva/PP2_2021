import pygame as pg
import random
pg.init()
pg.display.set_caption("AIBERGENOID_OOP")

WIDTH = 800
HEIGHT = 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LOCATIONS = {
    30:  [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    70: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    110: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]
}

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.radius = 20
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = -5
        self.surf = pg.Surface((self.r*2, self.r*2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=((self.x, self.y)))
        self.speed = 3
        self.draw()

    def move(self):
        self.rect.move_ip(self.dx, self.dy)

    def draw(self):
        pg.draw.circle(self.surf, (0, 0, 255), (self.r, self.r), self.r)
        screen.blit(self.surf, self.rect)


class Brick(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.surf = pg.Surface((40, 30))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(0, WIDTH - 50), 100))
        
    def draw(self):
        screen.blit(self.surf, self.rect)

class Play(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((400, 20))
        self.rect = self.surf.get_rect(center = ((WIDTH // 2, HEIGHT // 2 + 200)))
        self.speed = 40
    
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            if self.rect.right <= 0:
                self.rect.left = WIDTH
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_RIGHT]:
            if self.rect.left >= WIDTH:
                self.rect.right = 0
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        screen.blit(self.surf, self.rect)
        self.surf.fill('green')


B1 = Ball(WIDTH // 2, HEIGHT // 2 + 100)
P1 = Play()
entities = pg.sprite.Group([P1, B1])
bricks = pg.sprite.Group([Brick() for _ in range(5)])
for y, i in LOCATIONS.items:
    for j in i:


font = pg.font.SysFont("Times New Roman", 40, True)
score = 0
running = True
lose = False
mouse = False

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                mouse = not mouse

    screen.fill(WHITE)

    for entity in entities:
        entity.draw()
        entity.move()

    for b in bricks:
        b.draw()
    pg.draw.circle(screen, RED, (x_c, y_c), r)
    
    if pg.sprite.collide_rect(B1, P1):

    if x_c + r >= WIDTH or x_c - r <= 0:
        dx *= -1
        score += 1
    if y_c - r <= 0:
        dy *= -1
        score += 1

    x_c += dx
    y_c += dy

    if x <= 200:
        x = 200
    if x >= 600:
        x = 600

    if y_c >= HEIGHT:
        lose = True
        pg.mixer.music.stop()

    # pg.draw.rect(screen, BLUE, (x - 200, 500, 400, 20))

    ball_point = (x_c, y_c + r)
    # Collision of ball with blue thing
    if (ball_point[0] in range(x - 200, x + 200 + 1)) and (ball_point[1] >= 500):
        dy *= -1
        score += 1

    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                lose = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    x_c, y_c = WIDTH // 2, HEIGHT - 150
                    dx, dy = 4, -6
                    r = 30
                    score = 0
                    # pg.mixer.music.play(-1)
                    lose = False
                    running = True

        pg.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                     HEIGHT // 2 - 200, 400, 400))
        text1 = font.render('GAME OVER', False, False)
        text2 = font.render(f'Your score is: {score}', False, False)
        screen.blit(text1, (WIDTH // 2 - 200, HEIGHT // 2 - 200))
        screen.blit(text2, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        pg.display.flip()
    pg.display.flip()
pg.quit()