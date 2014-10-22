from random import randint, random
from time import time
import sys
import pygame
import pygame.locals

def Evolution(size, type):
	pygame.init()
	cellsize = 15
	screen = pygame.display.set_mode((size*cellsize, size*cellsize))
	grid = gridcreator(size, type)
	while True:
		grid = [[celltransitioner(size, grid, j, k) for k in range (size)] for j in range (size)]
		for i in range(size):
			for j in range(size):
				Int, Str, Agi = grid[i][j]
				net = Int + Str + Agi
				mini = min(Int, Str, Agi)
				Int, Str, Agi = int((255**2)*(Int - mini)/((255 - 3*mini)*net)), int((255**2)*(Str-mini)/((255 - 3*mini)*net)), int((255**2)*(Agi - mini)/((255 - 3*mini)*net))
				pygame.draw.rect(screen, pygame.Color(Int, Str, Agi), (i*cellsize, j*cellsize, cellsize, cellsize))
		for event in pygame.event.get():
			if event.type == pygame.locals.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.flip()
	acc = [0, 0, 0]
	for x in grid:
		for y in x:
			for l in range (3):
				acc[l] += y[l]
	print (acc)

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

def gridcreator(size, type):
	if type == 0:
		return [[(random(), random(), random()) for x in range (size)] for y in range (size)]
	elif type == 1:
		return [[(0, 75, 180) for x in range (size)] for y in range (size)]
	elif type == 2:
		return [[(255, 0, 0) for x in range (size)] for y in range (size)]
	elif type == 3:
		return ([[(0, 0, 255) for x in range (size)] for y in range (int(size/2))] + [[(255, 0, 0) for x in range (size)] for y in range (int(size/2))])

t1 = time()
Evolution(60, 0)
t2 = time()
print (t2-t1)
