import random


class Map:

	def __init__(self):
		# INITIAL HEIGHT AND WIDTH
		self.height = 10
		self.width = 8
		self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
					'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '&', '*']
		self.matrix = [[1 for _ in range(self.width+1)] for _ in range(self.height)]

	# generates the initial matrix of random integers from 0 to 300
	def create_matrix(self):
		# randomize the matrix content from 0 to 300
		for i in range(self.height):
			for j in range(self.width+1):
				self.matrix[i][j] = random.randint(0, 300)

		return self.matrix


	# prints the matrix in the screen, in a more readable way
	def print_matrix(self):

		# if the number is more than 100 turn it into 'III'
		# else if the number is less than 100 turn it into ' '
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if self.matrix[i][j] < 100:
					self.matrix[i][j] = ' '
				else:
					self.matrix[i][j] = 'XXX'

		# enumerates the rows and columns (rows = numbers, columns  = letters)
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])+1):
				self.matrix[i][0] = len(self.matrix)-i-1
				self.matrix[len(self.matrix)-1][j-1] = self.alphabet[j - 2]

		# prints the matrix
		for i in self.matrix:
			print('\t'.join(map(str, i)))


	# iterates all matrix values and adds a random number in between all cells
	def populate(self):
		aux2 = 0

		# creates the new rows to fit the new cells vertically and later horizontally
		for i in range(len(self.matrix)-1):
			aux2 += 1
			self.matrix.insert(i+aux2, [])

		# VERTICAL - adds new cells in between old cells vertically
		# the new cell is a random number between it's above and below cell
		for k in range(len(self.matrix)):
			if (k % 2) != 0:
				for j in range(len(self.matrix[0])):
					if (k+1) < (len(self.matrix)):
						a = self.matrix[k-1][j]
						b = self.matrix[k+1][j]
						if b > a:
							self.matrix[k].append((random.randint(a, b)))
						else:
							self.matrix[k].append((random.randint(b, a)))
			else:
				pass

		# updates the width to be used below
		width_ = (len(self.matrix[0])) - 1

		# HORIZONTAL - adds new cells in between old cells horizontally
		# the new cell is a random number between it's left and right cell
		for i in range(len(self.matrix)):
			aux = 0
			for j in range(width_):
				aux += 1
				a = self.matrix[i][j+aux-1]
				b = self.matrix[i][j+aux]
				if b > a:
					self.matrix[i].insert(j+aux, random.randint(a, b))
				else:
					self.matrix[i].insert(j+aux, random.randint(b, a))

		return self.matrix

	def return_matrix(self, populate, create_matrix, print_matrix):
		print_matrix(populate(populate(create_matrix())))
