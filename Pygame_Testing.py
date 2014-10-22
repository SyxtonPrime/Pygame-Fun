import sys
import pygame
import pygame.locals
from random import randint

def player():
	transition = 0
	type = 0
	if transition == 0:
		simple(type)

def simple(type):
	pygame.init
	cellsize = 20
	size = 50
	screen = pygame.display.set_mode((size*cellsize, size*cellsize))
	acc = 0
	grid = createGrid(size, type)
	while True:
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
				pygame.draw.rect(screen, pygame.Color(num*127, num*127, num*127)    , (i*cellsize, j*cellsize, cellsize, cellsize))
				newrow.append(num)
			newgrid.append(newrow)
		for event in pygame.event.get():
			if event.type == pygame.locals.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.flip()
		grid = newgrid

def createGrid(size, type):
	grid = []
	if type == 0:
		for i in range(size):
			row = []
			for j in range(size):
				row.append(randint(0, 2))
			grid.append(row)
	elif type == 1:
		grid = [[int((2*j - 1)/size) for j in range (size)] for x in range (size)]
	return (grid)
	
player()
