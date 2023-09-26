import random

#HEIGHT AND WIDTH CONSTANTS
height = 10
width = 10

#generates the initial matrix of random integers from 0 to 254
def createMatrix():

	matrix = [[ 1 for i in range(width+1)] for j in range(height)]

	#randomize the matrix content from 0 to 254
	for i in range(height):
		for j in range(width+1):
			matrix[i][j] = random.randint(0, 254)

	#enumerates the rows
	for i in range(height):
		for j in range(width+1):
			matrix[i][0] = i

	return matrix

#prints the matrix in the screen, in a more readable way
def printMatrix(matrix):
	for i in matrix:
		print('\t'.join(map(str, i)))

# iterates all matrix values and adds a random number in between all cells
def populate(matrix):
	printMatrix(matrix)
	aux = 1
	aux2 = 0

	for i in range(len(matrix)):
		aux2 += 1
		matrix.insert(i+aux2, [])

	#VERTICAL
	for k in range(len(matrix)):
		if (k % 2) != 0:
			for j in range(len(matrix[0])):
				matrix[k].append((random.randint(0, 254)))
		else:
			pass

	#HORIZONTAL
	for list in matrix:
		for j in range(len(list)-2):
			aux += 1
			list.insert(j+aux, random.randint(0, 254))


	return matrix


#printMatrix(createMatrix())

printMatrix(populate(createMatrix()))