import random

#height = 10
#width = 10

def createMatrix(height, width):
	matrix = [[0]*width]*height

	for j in range(height):
		for i in range(width):
			matrix[j][i] = 1

	for i in matrix:
		print('\t'.join(map(str, i)))

createMatrix(10, 10)