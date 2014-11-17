from random import randint, random
from time import time
import sys
import pygame
import pygame.locals

def Evolution(size, startgrid):
    pygame.init()
    cellsize = 15
    screen = pygame.display.set_mode((size*cellsize, size*cellsize))
    grid = gridcreator(size)
    count = 0
    extinction = False
    while True:
        count += 1
        grid = [[celltransitioner(size, grid, j, k) for k in range (size)] for j in range (size)]
        mass_extinction = random()
        if mass_extinction < count/1000000:
            grid = meteor(grid, size)
            count = 0
            extinction = False
        elif (mass_extinction < 1/600) | ((mass_extinction < 0.5) & extinction):
            grid = extinction_event(grid, size)
            extinction = True
        else:
            extinction = False
        for i in range(size):
            for j in range(size):
                Int, Str, Agi = grid[i][j]
                net = Int + Str + Agi
                mini = min(Int, Str, Agi)
                Int, Str, Agi = (int((255**2)*(Int - mini)/((255 - 3*mini)*net)),
                                 int((255**2)*(Str-mini)/((255 - 3*mini)*net)),
                                 int((255**2)*(Agi - mini)/((255 - 3*mini)*net)))
                pygame.draw.rect(screen, pygame.Color(Int, Str, Agi),
                                                 (i*cellsize, j*cellsize, cellsize, cellsize))
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def extinction_event(grid, size):
    '''Radically alter the grid'''
    startInt, startStr, startAgi, endInt, endStr, endAgi = 0,0,0,0,0,0
    death = random()
    bound = 100*(random())
    for row in range(size):
        for col in range(size):
            (Int, Str, Agi) = grid[col][row]
            startInt += Int
            startStr += Str
            startAgi += Agi
            if Int > Str:
                if Int > Agi:
                    Int *= random()**2/2
                    if Str > Agi:
                        Str *= random()/2
                    else:
                        Agi *= random()/2
                else:
                    Agi *= random()**2/2
                    Int *= random()/2
            else:
                if Str > Agi:
                    Str *= random()**2/2
                    if Int > Agi:
                        Int *= random()/2
                    else:
                        Agi *= random()/2
                else:
                    Agi *= random()**2/2
                    Str *= random()/2
            grid[col][row] = (Int, Str, Agi)
            endInt += Int
            endStr += Str
            endAgi += Agi
    print('Extinction', (int(startInt), int(startStr), int(startAgi)),(int(endInt), int(endStr), int(endAgi)),
        (int(startInt - endInt), int(startStr - endStr), int(startAgi - endAgi)),
        (int(100*(1 - endInt/startInt)), int(100*(1 - endStr/startStr)), int(100*(1 - endAgi/startAgi))))
    return grid

def meteor(grid, size):
    num = int(3*size/4)
    a = random()
    if a < 0.25:
        grid, startInt, startStr, startAgi, endInt, endStr, endAgi = meteorimpact(grid, size, 0, num, 0, num)
    elif a < 0.5:
        grid, startInt, startStr, startAgi, endInt, endStr, endAgi = meteorimpact(grid, size, 0, num, size-num, size)
    elif a < 0.75:
        grid, startInt, startStr, startAgi, endInt, endStr, endAgi = meteorimpact(grid, size, size-num, size, 0, num)
    else:
        grid, startInt, startStr, startAgi, endInt, endStr, endAgi = meteorimpact(grid, size, size-num, size, size-num, size)
    print('Meteor', (int(startInt), int(startStr), int(startAgi)),(int(endInt), int(endStr), int(endAgi)),
        (int(startInt - endInt), int(startStr - endStr), int(startAgi - endAgi)),
        (int(100*(1 - endInt/startInt)), int(100*(1 - endStr/startStr)), int(100*(1 - endAgi/startAgi))))
    return grid

def meteorimpact(grid, size, minx, maxx, miny, maxy):
    startInt, startStr, startAgi, endInt, endStr, endAgi = 0,0,0,0,0,0
    for i in range (size):
        for j in range (size):
            Int, Str, Agi = grid[i][j]
            startInt += Int
            startStr += Str
            startAgi += Agi
            if (minx <= i <= maxx) & (miny <= j <= maxy):
                grid[i][j] = (0.001, 0.001, 0.001)
                endInt += 0.001
                endStr += 0.001
                endAgi += 0.001
            else:
                scalar = random()/4
                grid[i][j] = (scalar*Int, scalar*Str, scalar*Agi)
                endInt += scalar*Int
                endStr += scalar*Str
                endAgi += scalar*Agi
    return (grid, startInt, startStr, startAgi, endInt, endStr, endAgi)

def celltransitioner(size, grid, j, k):
    inc = random()
    Int, Str, Agi = grid[j][k]
    avInt, avStr, avAgi = 0, 0, 0
    num = 0
    if k == 0:
        cell = grid[j][k+1]
        avInt += cell[0]
        avStr += cell[1]
        avAgi += cell[2]
        num += 1
    elif k == (size - 1):
        cell = grid[j][k-1]
        avInt += cell[0]
        avStr += cell[1]
        avAgi += cell[2]
        num += 1
    else:
        cell1, cell2 = grid[j][k+1], grid[j][k-1]
        avInt += cell1[0] + cell2[0]
        avStr += cell1[1] + cell2[1]
        avAgi += cell1[2] + cell2[2]
        num += 2
    if j == 0:
        cell = grid[j+1][k]
        avInt += cell[0]
        avStr += cell[1]
        avAgi += cell[2]
        num += 1
    elif j == (size - 1):
        cell = grid[j-1][k]
        avInt += cell[0]
        avStr += cell[1]
        avAgi += cell[2]
        num += 1
    else:
        cell1, cell2 = grid[j+1][k], grid[j-1][k]
        avInt += cell1[0] + cell2[0]
        avStr += cell1[1] + cell2[1]
        avAgi += cell1[2] + cell2[2]
        num += 2
    avInt /= num
    avStr /= num
    avAgi /= num
    if (Int < avInt):
        if (Str < avStr):
            if (Agi < avAgi):
                nInt, nStr, nAgi = (Int + inc, Str + inc, Agi + inc)
            else:
                if avInt > avStr:
                    nInt, nStr, nAgi = (Int + inc, Str, Agi)
                else:
                    nInt, nStr, nAgi = (Int, Str + inc, Agi)
        elif (Agi < avAgi):
            if avInt > avAgi:
                nInt, nStr, nAgi = (Int + inc, Str, Agi)
            else:
                nInt, nStr, nAgi = (Int, Str, Agi + inc)
        else:
            if inc < 0.01:
                # Choose your own adventure: 
                # nInt, nStr, nAgi = (inc, inc, inc)
                # nInt, nStr, nAgi = (random(), random(), random())
                nInt, nStr, nAgi = ((1.5)*random()*avInt, (1.5)*random()*avStr, (1.5)*random()*avAgi)
                # nInt, nStr, nAgi = (avInt, avStr, avAgi)
            else:
                nInt, nStr, nAgi = (Int, Str, Agi)
    elif (Str < avStr) & (Agi < avAgi):
        if avStr > avAgi:
            nInt, nStr, nAgi = (Int, Str + inc, Agi)
        else:
            nInt, nStr, nAgi = (Int, Str, Agi + inc)
    else:
        if inc < 0.01:
            # Choose your own adventure:
            # nInt, nStr, nAgi = (inc, inc, inc)
            # nInt, nStr, nAgi = (random(), random(), random())
            nInt, nStr, nAgi = ((1.5)*random()*avInt, (1.5)*random()*avStr, (1.5)*random()*avAgi)
            # nInt, nStr, nAgi = (avInt, avStr, avAgi)
        else:
            nInt, nStr, nAgi = (Int, Str, Agi)
    # power = (nInt + nStr + nAgi)/2
    # nInt, nStr, nAgi = (nInt/power, nStr/power, nAgi/power)
    return((nInt, nStr, nAgi))

def gridcreator(size):
        return [[(random(), random(), random()) for x in range (size)] for y in range (size)]

t1 = time()
Evolution(50, 0)
t2 = time()
print (t2-t1)
