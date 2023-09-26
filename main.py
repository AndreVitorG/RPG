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
	for i in range(len(matrix)):
		for j in range(len(matrix[0])+1):
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
				if k+1 < (len(matrix)):
					a = matrix[k-1][j]
					b = matrix[k+1][j]
					if b > a:
						matrix[k].append((random.randint(a, b)))
					else:
						matrix[k].append((random.randint(b, a)))
		else:
			pass

	#HORIZONTAL
	for list in matrix:
		for j in range(len(list)-2):
			aux += 1
			a = j+aux-1
			b = j+aux+1
			if b > a:
				list.insert(j+aux, random.randint(a, b))
			else:
				list.insert(j+aux, random.randint(b, a))


	return matrix


#printMatrix(createMatrix())

#printMatrix(populate(createMatrix()))

printMatrix(populate(populate(createMatrix())))