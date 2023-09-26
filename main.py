import random

#HEIGHT AND WIDTH CONSTANTS
height = 5
width = 5

#generates the initial matrix of random integers from 0 to 254
def createMatrix():

	matrix = [[ 1 for i in range(width+1)] for j in range(height)]

	#randomize the matrix content from 0 to 254
	for i in range(height):
		for j in range(width+1):
			matrix[i][j] = random.randint(0, 254)

	#enumerates the rows (colocar na hora de printar!!!!!!!!!!!!!!!!!!!!!!!)
#	for i in range(len(matrix)):
#		for j in range(len(matrix[0])+1):
#			matrix[i][0] = i

	return matrix

#prints the matrix in the screen, in a more readable way
def printMatrix(matrix):

 #   	for i in range(len(matrix)):
  #      	for j in range(len(matrix[0])):
   #        		if matrix[i][j] < 100:
    #         			matrix[i][j] = '-'
     #      		else:
      #        			matrix[i][j] = 'X'
	
	for i in matrix:
		print('\t'.join(map(str, i)))


# iterates all matrix values and adds a random number in between all cells
def populate(matrix):
#	printMatrix(matrix)
#	print(" ")
	aux2 = 0

	for i in range(len(matrix)-1):
		aux2 += 1
		matrix.insert(i+aux2, [])


	#VERTICAL  --  funciona
	for k in range(len(matrix)):
		if (k % 2) != 0:
			for j in range(len(matrix[0])):
				if (k+1) < (len(matrix)):
					a = matrix[k-1][j]
##					print(a)
					b = matrix[k+1][j]
##					print(b)
##					printMatrix(matrix)
##					print(len(matrix))
					if b > a:
						matrix[k].append((random.randint(a, b)))
					else:
						matrix[k].append((random.randint(b, a)))
##				elif k+2 > len(matrix) or k > len(matrix):
##					pass
		else:
			pass
			
	#define a width para ser usada na próxima função(seria -2 se a enumeração das rows estivesse ativa, se for ativa apenas na hora de printar n precisa)		
	width = (len(matrix[0]))-1

    
    #HORIZONTAL  --  funciona, mas pela metade (no eixo x) no segundo populate
	for i in range(len(matrix)):
		aux = 0
		for j in range((width)):
#			printMatrix(matrix)
			aux += 1
##			print(j+aux-1)
			a = matrix[i][j+aux-1]
##			print(a)
			b = matrix[i][j+aux]
##			print(b)
			if b > a:
				matrix[i].insert(j+aux, random.randint(a, b))
			else:
				matrix[i].insert(j+aux, random.randint(b, a))

	return matrix


#printMatrix(createMatrix())

#printMatrix(populate(createMatrix()))

#mat = createMatrix()
#printMatrix(mat)
#mat1 = populate(mat)
#printMatrix(mat1)
#mat2 = populate(mat1)
#printMatrix(mat2)

printMatrix(populate(populate(createMatrix())))
