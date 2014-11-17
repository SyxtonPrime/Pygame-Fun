import sys
import pygame
import pygame.locals
from random import randint

def player():
    pygame.init
    transition = 0
    startgrid = 0
    numcolours = 6
    cellsize = 15
    size = 60
    screen = pygame.display.set_mode((size*cellsize, size*cellsize))
    acc = 0
    grid = createGrid(size, startgrid, numcolours)
    if transition == 0:
        simple(size, grid, cellsize, screen, numcolours)

def simple(size, grid, cellsize, screen, numcolours):
    clock = pygame.time.Clock()
    while True:
        clock.tick()
        # print('{:.0f} FPS'.format(clock.get_fps()))
        newgrid = []
        for i in range(size):
            newrow = []
            for j in range(size):
                a = randint(0, 3)
                if a == 0:
                    num = grid[i-1][j]
                if a == 1:
                    num = grid[i][j-1]
                if a == 2:
                    num = grid[(i+1)%(size)][j]
                if a == 3:
                    num = grid[i][(j+1)%(size)]
                colour = int(255*num/(numcolours - 1))
                pygame.draw.rect(screen, pygame.Color(colour, colour, colour),
                    (i*cellsize, j*cellsize, cellsize, cellsize))
                newrow.append(num)
            newgrid.append(newrow)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        grid = newgrid

def createGrid(size, startgrid, numcolours):
    if startgrid == 0:
        return [[randint(0, numcolours - 1) for j in range(size)] for i in range(size)]
    elif startgrid == 1:
        return [[int((2*j - 1)/size) for j in range (size)] for x in range (size)]

player()
