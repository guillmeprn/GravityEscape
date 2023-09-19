import pygame
from pygame.locals import *
from Item.Item2D import Item2D
from Bloc.GravityBloc import *
from Bloc.StaticBloc import *
from Player import Player
from Level import Level

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Gravity Escape")

clock = pygame.time.Clock()
dt = 0

floor = GravityItem((500, 700), (1000, 100))
roof = GravityItem((500, 0), (1000, 100))

list_bloc = []

level = Level("level", window)

def shoot(x, y):

    s = Item2D((x, y), (5, 5))

    for b in list_bloc:
        if(b.testCollisionWithOtherItem(s)):
            print("Invert", b)
            b.invertGravity()
            return True

    return False

inGame = True

player = Player((200, 200))

while inGame:
    for event in pygame.event.get():
        if event.type == QUIT:
            inGame = False
        if event.type == MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            if not shoot(posX, posY):
                list_bloc.append(GravityBloc((posX, posY)))

    window.fill((0, 0, 0))

    floor.display(window)
    roof.display(window)

    level.update()

    for b in list_bloc:
        b.display(window)
        b.move(dt)

    player.display(window)
    player.move(dt)

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if(keys[K_SPACE]):
        player.jump()

    if(keys[K_d] or keys[K_RIGHT]):
        player.goRight(dt)

    if(keys[K_q] or keys[K_LEFT]):
        player.goLeft(dt)

    dt = clock.tick(60)

pygame.quit()
