import pygame
import time
from random import randint
pygame.init()

mw = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rand = 0
rand1 = 0


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, other_rect):
        return self.rect.colliderect(other_rect)

class Picture(Area):
    def __init__(self, filename, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        rand = randint(1, 4)
        if rand == 1 and G.rect.x < K.rect.x:
            self.rect.x += randint(0, 3)
        else:
            self.rect.x -= randint(0, 3)
        if rand == 2 and G.rect.x > K.rect.x:
            self.rect.y += randint(0, 3)
        else:
            self.rect.x += randint(0, 3)
        if rand == 3:
            self.rect.x -= randint(0, 3)
        if rand == 4:
            self.rect.y -= randint(0, 3)

x_k = randint(50, 450)
x_y = randint(50, 450)
win = False
move_left = False
move_right = False
move_up = False
move_down = False

G = Picture('p.png', 100, 100, 50, 50, (255, 255, 255))
K = Picture('k.png', x_k, x_y, 30, 30, (255, 255, 255))
b = Picture('b.png', 0, 0, 500, 500, (255, 255, 255))
b1 = Picture('b1.png', 0, 0, 500, 500, (255, 255, 255))

while win == False:
    x_k = randint(50, 450)
    x_y = randint(50, 450)
    mw.fill((255, 255, 255))
    rand1 = randint(1,6)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if K.rect.x > 500:
        K.rect.x = x_k
        K.rect.y = x_y

    if K.rect.x < 0:
        K.rect.x = x_k
        K.rect.y = x_y

    if K.rect.y > 500:
        K.rect.y = x_y
        K.rect.x = x_k

    if K.rect.y < 0:
        K.rect.y = x_y
        K.rect.x = x_k

    if move_right:
        G.rect.x += 2.5
    if move_left:
        G.rect.x -= 2.5
    if move_down:
        G.rect.y += 2.5
    if move_up:
        G.rect.y -= 2.5
    if win == False:
        b.draw()

    if rand1 == 1:
        for i in range(25):
            K.move()

    if G.rect.colliderect(K.rect):
        win = True
        b1.draw()
    
    
    K.draw()
    G.draw()

    clock.tick(40)
    pygame.display.update()
