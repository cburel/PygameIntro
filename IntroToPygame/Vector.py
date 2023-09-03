import math

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#converts vector to pretty string
	def __str__(self):
		return("Vector: " + str(self.x) + ", " + str(self.y))

	#overloads + operator to add two vectors
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	#overloads - operator to subtract two vectors
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	#returns the dot product of two vectors
	def dot(self, other):
		return ((self.x * other.x) + (self.y * other.y))

	#scales the vector by a float and returns scaled vector
	def scale(self, scalar):
		return (self.x * scalar, self.y * scalar)

	#returns the length (magnitude) of a vector
	def length(self):
		return (math.sqrt((self.x**2) + (self.y ** 2)))

	#returns the normalized version of a vector
	def normalize(self):
		if self.length() == 0:
			return Vector(0,0)
		else:
			return Vector(self.x/self.length(), self.y/self.length())