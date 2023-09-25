import random

#height = 10
#width = 10


def createMatrix(height, width):

	matrix = [[ 1 for i in range(height)] for j in range(width)]

	for i in range(height):
		for j in range(width):
			matrix[i][j] = random.randint(0, 254)

	return matrix


def printMatrix(matrix):
	for i in matrix:
		print('\t'.join(map(str, i)))


def populate(matrix):



populate(createMatrix(10, 10))