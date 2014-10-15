import sys
import pygame
import pygame.locals
from random import randint

def simple():
	pygame.init
	cellsize = 40
	size = 20
	screen = pygame.display.set_mode((size*cellsize, size*cellsize))
	acc = 0
	grid = createGrid(size)
	while True:
		for i in range(size):
			for j in range(size):
				if grid[i][j] == 1:
					pygame.draw.rect(screen, pygame.Color(255, 255, 255), (i*cellsize, j*cellsize, cellsize, cellsize))
				else:
					pygame.draw.rect(screen, pygame.Color(0, 0, 0), (i*cellsize, j*cellsize, cellsize, cellsize))
		for event in pygame.event.get():
			if event.type == pygame.locals.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.flip()

def createGrid(size):
	grid = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(randint(0, 1))
		grid.append(row)
	return(grid)

			
simple()
