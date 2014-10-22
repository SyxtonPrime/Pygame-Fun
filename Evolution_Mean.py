from random import randint, random
from time import time
import sys
import pygame
import pygame.locals

def Evolution(size, type):
	pygame.init()
	inc = 10
	cellsize = 15
	screen = pygame.display.set_mode((size*cellsize, size*cellsize))
	grid = gridcreator(size, type)
	while True:
		grid = [[celltransitioner(size, grid, j, k, inc) for k in range (size)] for j in range (size)]
		for i in range(size):
			for j in range(size):
				Int, Str, Agi = grid[i][j]
				mini = min(Int, Str, Agi) - 5
				Int, Str, Agi = int(255*(Int - mini)/(255 - 3*mini)), int(255*(Str-mini)/(255 - 3*mini)), int(255*(Agi - mini)/(255 - 3*mini))
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

def celltransitioner(size, grid, j, k, inc):
	inc += randint(0, 2)
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
	if (Int == avInt) & (Str == avStr): # If these are true then Agi == avAgi
		num = randint(0, 5)
		if num == 0:
			nInt, nStr, nAgi = (Int + inc, Str, Agi - inc)
		elif num == 1:
			nInt, nStr, nAgi = (Int, Str + inc, Agi - inc)
		elif num == 2:
			nInt, nStr, nAgi = (Int + inc, Str - inc, Agi)
		elif num == 3:
			nInt, nStr, nAgi = (Int, Str - inc, Agi + inc)
		elif num == 4:
			nInt, nStr, nAgi = (Int - inc, Str + inc, Agi)
		elif num == 5:
			nInt, nStr, nAgi = (Int - inc, Str, Agi + inc)
	elif (Int <= avInt):
		if (Str <= avStr):
			if random() > 0.5:
				nInt, nStr, nAgi = (Int + inc, Str, Agi - inc)
			else:
				nInt, nStr, nAgi = (Int, Str + inc, Agi - inc)
		elif (Agi <= avAgi):
			if random() > 0.5:
				nInt, nStr, nAgi = (Int + inc, Str - inc, Agi)
			else:
				nInt, nStr, nAgi = (Int, Str - inc, Agi + inc)
		else:
			nInt, nStr, nAgi = (Int, Str, Agi)
	elif (Str <= avStr) & (Agi <= avAgi):
		if random() > 0.5:
			nInt, nStr, nAgi = (Int - inc, Str + inc, Agi)
		else:
			nInt, nStr, nAgi = (Int - inc, Str, Agi + inc)
	else:
		nInt, nStr, nAgi = (Int, Str, Agi)
	if (nInt < 0):
		nInt += inc
		if nStr>nAgi:
			nStr -= inc
		else:
			nAgi -= inc
	elif (nStr < 0):
		nStr += inc
		if nInt>nAgi:
			nInt -= inc
		else:
			nAgi -= inc
	elif (nAgi < 0):
		nAgi += inc
		if nInt>nStr:
			nInt -= inc
		else:
			nStr -= inc
	return((nInt, nStr, nAgi))

def gridcreator(size, type):
	if type == 0:
		return [[(85, 85, 85) for x in range (size)] for y in range (size)]
	elif type == 1:
		return [[(0, 75, 180) for x in range (size)] for y in range (size)]
	elif type == 2:
		return [[(255, 0, 0) for x in range (size)] for y in range (size)]
	elif type == 3:
		return ([[(0, 0, 255) for x in range (size)] for y in range (int(size/2))] + [[(255, 0, 0) for x in range (size)] for y in range (int(size/2))])

t1 = time()
Evolution(40, 0)
t2 = time()
print (t2-t1)
