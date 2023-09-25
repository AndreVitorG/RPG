import random

height = 10
width = 10


def createMatrix():

	matrix = [[ 1 for i in range(width+1)] for j in range(height)]

	for i in range(height):
		for j in range(width+1):
			matrix[i][j] = random.randint(0, 254)

	for i in range(height):
		for j in range(width+1):
			matrix[i][0] = i

	return matrix


def printMatrix(matrix):
	for i in matrix:
		print('\t'.join(map(str, i)))


def populate(matrix):
	printMatrix(matrix)
	aux = 1
	for list in matrix:
		for j in range(len(list)):
			aux += 1
			list.insert(j+aux, random.randint(0, 254))


	return matrix


#printMatrix(createMatrix())

printMatrix(populate(createMatrix()))