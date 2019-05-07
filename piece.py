from enum import Enum
import numpy as np

class Piece:

	def __init__(self, color, name): 
		self.color = color
		self.set_shape(name)
		self.name = name

	def set_shape(self, name):
		if name == "ONE":
			self.shape = np.array([[1]]) * self.color
		elif name == "TWO":
			self.shape = np.array([[1,1]]) * self.color
		elif name == "THREE":
			self.shape = np.array([[1,1,1]]) * self.color
		elif name == "FOUR":
			self.shape = np.array([[1,1,1,1]]) * self.color
		elif name == "FIVE":
			self.shape = np.array([[1,1,1,1,1]]) * self.color
		elif name == "SHORT_CORNER":
			self.shape = np.array([[1,1], [0,1]]) * self.color
		elif name == "SQUARE":
			self.shape = np.array([[1,1], [1,1]]) * self.color
		elif name == "SHORT_T":
			self.shape = np.array([[0,1,0], [1,1,1]]) * self.color
		elif name == "SHORT_L":
			self.shape = np.array([[0,0,1], [1,1,1]]) * self.color
		elif name == "S":
			self.shape = np.array([[0,1,1], [1,1,0]]) * self.color
		elif name == "LONG_L":
			self.shape = np.array([[1,0,0,0], [1,1,1,1]]) * self.color
		elif name == "LONG_T":
			self.shape = np.array([[0,1,0], [0,1,0], [1,1,1]]) * self.color
		elif name == "LONG_CORNER":
			self.shape = np.array([[1,0,0], [1,0,0], [1,1,1]]) * self.color
		elif name == "RIFLE":
			self.shape = np.array([[0,1,1,1], [1,1,0,0]]) * self.color
		elif name == "Z":
			self.shape = np.array([[0,0,1], [1,1,1], [1,0,0]]) * self.color 
		elif name == "UTAH":
			self.shape = np.array([[1,0], [1,1], [1,1]]) * self.color
		elif name == "W":
			self.shape = np.array([[0,1,1], [1,1,0], [1,0,0]]) * self.color 
		elif name == "U":
			self.shape = np.array([[1,1], [1,0], [1,1]]) * self.color 
		elif name == "F":
			self.shape = np.array([[0,1,1], [1,1,0], [0,1,0]]) * self.color
		elif name == "CROSS":
			self.shape = np.array([[0,1,0], [1,1,1], [0,1,0]]) * self.color
		elif name == "BIRD":
			self.shape = np.array([[0,1,0,0], [1,1,1,1]]) * self.color

	def rotate(self):
		self.shape = np.array(list(zip(*self.shape[::-1])))

	def flip(self):
		self.shape = np.flip(self.shape, 0)

	def get_shape(self):
		return self.shape

	def get_color(self):
		return self.color

	def get_name(self):
		return self.name


