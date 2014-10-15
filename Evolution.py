def Evolution(size, reps):
	from random import randint
	from PIL import Image
	stImg = Image.new('RGB', (size, size), "black")
	enImg = Image.new('RGB', (size, size), "black")
	grid = []
	decider = 0# Switches between different modes of Generation.
	for i in range (size): #Creates the starting grid of Creatures.
		row = []
		for j in range (size):
			if decider == 1:
				num = randint(5, 10)
				a = randint(0, 2)
				if a == 0:
					Int = num
					Str = randint(0, 15-Int)
					Agil = 15 - Int - Str
				elif a == 1:
					Str = num
					Agil = randint(0, 15-Str)
					Int = 15 - Str - Agil
				else:
					Agil = num
					Int = randint(0, 15-Agil)
					Str = 15 - Agil - Int
			elif decider == 2:
				a = randint(0, 6)
				if a == 0:
					(Int, Str, Agil) = (5, 5, 5)
				elif a == 1:
					(Int, Str, Agil) = (6, 4, 5)
				elif a == 2:
					(Int, Str, Agil) = (6, 5, 4)
				elif a == 3:
					(Int, Str, Agil) = (5, 6, 4)
				elif a == 4:
					(Int, Str, Agil) = (4, 6, 5)
				elif a == 5:
					(Int, Str, Agil) = (5, 4, 6)
				elif a == 6:
					(Int, Str, Agil) = (4, 5, 6)
			else:
				(Int, Str, Agil) = (5,5,5)
			row.append((Int, Str, Agil))
		grid.append(row)
	# for i in range (size): #Prints the grid out as a Matrix
		# print (grid[i])
	for i in range (0, size):
		for j in range (0, size):
			Int = grid[i][j][0]
			Str = grid[i][j][1]
			Agil = grid[i][j][2]
			stImg.putpixel((i, j), (25*Int, 25*Str, 25*Agil))
	stImg.show()
	for i in range (reps):
		newgrid = []
		for j in range (size):
			newrow = []
			for k in range(size):
				org = grid[j][k]
				avorg = [0, 0, 0, 0]
				if k == 0:
					for l in range (3):
						avorg[l] += grid[j][(k+1)][l]
					avorg[3] += 1
				elif k == (size - 1):
					for l in range (3):
						avorg[l] += grid[j][(k-1)][l]
					avorg[3] += 1
				else:
					for l in range (3):
						avorg[l] += grid[j][(k+1)][l]
						avorg[l] += grid[j][(k-1)][l]
					avorg[3] += 2
				if j == 0:
					for l in range (3):
						avorg[l] += grid[j+1][(k)][l]
					avorg[3] += 1
				elif j == (size - 1):
					for l in range (3):
						avorg[l] += grid[j-1][(k)][l]
					avorg[3] += 1
				else:
					for l in range (3):
						avorg[l] += grid[j+1][(k)][l]
						avorg[l] += grid[j-1][(k)][l]
					avorg[3] += 2
				avorg = (avorg[0]/avorg[3], avorg[1]/avorg[3], avorg[2]/avorg[3])
				if (org[0] == avorg[0]) & (org[1] == avorg[1]) & (org[2] == avorg[2]):
					num = randint(0, 5)
					if num == 0:
						newrow.append((org[0] + 1, org[1], org[2] - 1))
					elif num == 1:
						newrow.append((org[0], org[1] + 1, org[2] - 1))
					elif num == 2:
						newrow.append((org[0] + 1, org[1] - 1, org[2]))
					elif num == 3:
						newrow.append((org[0], org[1] - 1, org[2] + 1))
					elif num == 4:
						newrow.append((org[0] - 1, org[1] + 1, org[2]))
					elif num == 5:
						newrow.append((org[0] - 1, org[1], org[2] + 1))
				elif (org[0] <= avorg[0]) & (org[1] <= avorg[1]):
					if randint(0, 1) == 0:
						newrow.append((org[0] + 1, org[1], org[2] - 1))
					else:
						newrow.append((org[0], org[1] + 1, org[2] - 1))
				elif (org[0] <= avorg[0]) & (org[2] <= avorg[2]):
					if randint(0, 1) == 0:
						newrow.append((org[0] + 1, org[1] - 1, org[2]))
					else:
						newrow.append((org[0], org[1] - 1, org[2] + 1))
				elif (org[1] <= avorg[1]) & (org[2] <= avorg[2]):
					if randint(0, 1) == 0:
						newrow.append((org[0] - 1, org[1] + 1, org[2]))
					else:
						newrow.append((org[0] - 1, org[1], org[2] + 1))
				else:
					newrow.append(org)
			newgrid.append(newrow)
		grid = newgrid
		if i%2500 == 0:
			for i in range (0, size):
				for j in range (0, size):
					Int = grid[i][j][0]
					Str = grid[i][j][1]
					Agil = grid[i][j][2]
					if Int > 10:
						Int = 10
					elif Int < 0:
						Int = 0
					if Str > 10:
						Str = 10
					elif Str < 0:
						Str = 0
					if Agil > 10:
						Agil = 10
					elif Agil < 0:
						Agil = 0
					enImg.putpixel((i, j), (25*Int, 25*Str, 25*Agil))
			enImg.show()

	# print (reps)
	# for i in range (size): #Prints the final grid out as a Matrix
			# print (grid[i])
	for i in range (0, size):
		for j in range (0, size):
			Int = grid[i][j][0]
			Str = grid[i][j][1]
			Agil = grid[i][j][2]
			if Int > 10:
				Int = 10
			elif Int < 0:
				Int = 0
			if Str > 10:
				Str = 10
			elif Str < 0:
				Str = 0
			if Agil > 10:
				Agil = 10
			elif Agil < 0:
				Agil = 0
			enImg.putpixel((i, j), (25*Int, 25*Str, 25*Agil))
	enImg.show()
	pass

Evolution(10, 10000)
