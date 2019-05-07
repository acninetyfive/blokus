from enum import Enum
import numpy as np

class Piece:

	def __init__(self, color, shape): 
		self.color = color
		self.set_shape(shape)

	def set_shape(self, shape):
		if shape == "ONE":
			self.shape = np.array([[1]]) * self.color
		elif shape == "TWO":
			self.shape = np.array([[1,1]]) * self.color
		elif shape == "THREE":
			self.shape = np.array([[1,1,1]]) * self.color
		elif shape == "FOUR":
			self.shape = np.array([[1,1,1,1]]) * self.color
		elif shape == "FIVE":
			self.shape = np.array([[1,1,1,1,1]]) * self.color
		elif shape == "SHORT_CORNER":
			self.shape = np.array([[1,1], [0,1]]) * self.color
		elif shape == "SQUARE":
			self.shape = np.array([[1,1], [1,1]]) * self.color
		elif shape == "SHORT_T":
			self.shape = np.array([[0,1,0], [1,1,1]]) * self.color
		elif shape == "SHORT_L":
			self.shape = np.array([[0,0,1], [1,1,1]]) * self.color
		elif shape == "S":
			self.shape = np.array([[0,1,1], [1,1,0]]) * self.color
		elif shape == "LONG_L":
			self.shape = np.array([[1,0,0,0], [1,1,1,1]]) * self.color
		elif shape == "LONG_T":
			self.shape = np.array([[0,1,0], [0,1,0], [1,1,1]]) * self.color
		elif shape == "LONG_CORNER":
			self.shape = np.array([[1,0,0], [1,0,0], [1,1,1]]) * self.color
		elif shape == "RIFLE":
			self.shape = np.array([[0,1,1,1], [1,1,0,0]]) * self.color
		elif shape == "Z":
			self.shape = np.array([[0,0,1], [1,1,1], [1,0,0]]) * self.color 
		elif shape == "UTAH":
			self.shape = np.array([[1,0], [1,1], [1,1]]) * self.color
		elif shape == "W":
			self.shape = np.array([[0,1,1], [1,1,0], [1,0,0]]) * self.color 
		elif shape == "U":
			self.shape = np.array([[1,1], [1,0], [1,1]]) * self.color 
		elif shape == "F":
			self.shape = np.array([[0,1,1], [1,1,0], [0,1,0]]) * self.color
		elif shape == "CROSS":
			self.shape = np.array([[0,1,0], [1,1,1], [0,1,0]]) * self.color
		elif shape == "BIRD":
			self.shape = np.array([[0,1,0,0], [1,1,1,1]]) * self.color

	def rotate(self):
		self.shape = np.array(list(zip(*self.shape[::-1]) * self.color))

	def flip(self):
		self.shape = np.flip(self.shape, 0)

	def get_shape(self):
		return self.shape

	def get_color(self):
		return self.color
