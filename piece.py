from enum import Enum
import numpy as np

class Piece:

	def __init__(self, color, name): 
		self.color = color
		self.name = name
		self.set_shape()
		self.set_legal_moves()
		

	def set_shape(self):
		if self.name == "ONE":
			self.shape = np.array([[1]]) * self.color
		elif self.name == "TWO":
			self.shape = np.array([[1,1]]) * self.color
		elif self.name == "THREE":
			self.shape = np.array([[1,1,1]]) * self.color
		elif self.name == "FOUR":
			self.shape = np.array([[1,1,1,1]]) * self.color
		elif self.name == "FIVE":
			self.shape = np.array([[1,1,1,1,1]]) * self.color
		elif self.name == "SHORT_CORNER":
			self.shape = np.array([[1,1], [0,1]]) * self.color
		elif self.name == "SQUARE":
			self.shape = np.array([[1,1], [1,1]]) * self.color
		elif self.name == "SHORT_T":
			self.shape = np.array([[0,1,0], [1,1,1]]) * self.color
		elif self.name == "SHORT_L":
			self.shape = np.array([[0,0,1], [1,1,1]]) * self.color
		elif self.name == "S":
			self.shape = np.array([[0,1,1], [1,1,0]]) * self.color
		elif self.name == "LONG_L":
			self.shape = np.array([[0,0,0,1], [1,1,1,1]]) * self.color
		elif self.name == "LONG_T":
			self.shape = np.array([[0,1,0], [0,1,0], [1,1,1]]) * self.color
		elif self.name == "LONG_CORNER":
			self.shape = np.array([[1,1,1], [0,0,1], [0,0,1] ]) * self.color
		elif self.name == "RIFLE":
			self.shape = np.array([[0,1,1,1], [1,1,0,0]]) * self.color
		elif self.name == "Z":
			self.shape = np.array([[0,0,1], [1,1,1], [1,0,0]]) * self.color 
		elif self.name == "UTAH":
			self.shape = np.array([[1,0], [1,1], [1,1]]) * self.color
		elif self.name == "W":
			self.shape = np.array([[0,1,1], [1,1,0], [1,0,0]]) * self.color 
		elif self.name == "U":
			self.shape = np.array([[1,1], [1,0], [1,1]]) * self.color 
		elif self.name == "F":
			self.shape = np.array([[0,1,1], [1,1,0], [0,1,0]]) * self.color
		elif self.name == "CROSS":
			self.shape = np.array([[0,1,0], [1,1,1], [0,1,0]]) * self.color
		elif self.name == "BIRD":
			self.shape = np.array([[0,1,0,0], [1,1,1,1]]) * self.color

	def set_legal_moves(self):
		if self.name == "ONE":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-1), (-1,-1)]}
		elif self.name == "TWO":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-2), (-1,-2)],
			"r":[(1,1), (-2,1), (1,-1), (-2,-1)]}
		elif self.name == "THREE":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-3), (-1,-3)],
			"r":[(1,1), (-3,1), (1,-1), (-3,-1)]}
		elif self.name == "FOUR":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-4), (-1,-4)],
			"r":[(1,1), (-4,1), (1,-1), (-4,-1)]}
		elif self.name == "FIVE":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-5), (-1,-5)],
			"r":[(1,1), (-5,1), (1,-1), (-5,-1)]}
		elif self.name == "SHORT_CORNER":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-2), (-2,-2), (-2,0)],
			"r":[(1,0), (0,1), (-2,1), (-2,-2), (1,-2)],
			"rr":[(1,1), (-2,1), (-2,-2), (0,-2), (1,-1)],
			"rrr":[(1,1), (-2,1), (-2,-1), (-1,-2), (1,-2)]}
		elif self.name == "SQUARE":
			self.legal_moves = {
			"":[(1,1), (-2,1), (1,-2), (-2,-2)]}
		elif self.name == "SHORT_T":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-2,-3), (0,-3), (1,-2)],
			"r":[(1,1), (-3,1), (-3,-1), (-2,-2), (0,-2), (1,-1)],
			"rr":[(1,1), (-1,1), (-2,0), (-2,-2), (-1,-3), (1,-3)],
			"rrr":[(1,0), (0,1), (-2,1), (-3,0), (-3,-2), (1,-2)]}
		elif self.name == "SHORT_L":
			self.legal_moves = {
			"":[(1,-1), (0,1), (-2,1), (-2,-3), (1,-3)],
			"r":[(1,1), (-3,1), (-3,-2), (-1,-2), (1,-1)],
			"rr":[(1,1), (-2,1), (-2,-1), (-1,-3), (1,-3)],
			"rrr":[(1,1), (-1,1), (-3,0), (-3,-2), (1,-2)],
			"f":[(1,1), (-1,1), (-2,-1), (-2,-3), (1,-3)],
			"fr":[(1,0), (-1,1), (-3,1), (-3,-2), (1,-2)],
			"frr":[(1,1), (-2,1), (-2,-3), (0,-3), (1,-1)],
			"frrr":[(1,1), (-3,1), (-3,-1), (-1,-2), (1,-2)]}
		elif self.name == "S":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-2,-2), (-1,-3), (1,-3)],
			"r":[(1,1), (-2,1), (-3,0), (-3,-2), (0,-2), (1,-1)],
			"f":[(1,1), (-1,1), (-2,0), (-2,-3), (0,-3), (1,-2)],
			"fr":[(1,0), (0,1), (-3,1), (-3,-1), (-2,-2), (1,-2)]}
		elif self.name == "LONG_L":
			self.legal_moves = {
			"":[(1,-2), (0,1), (-2,1), (-2,-4), (1,-4)],
			"r":[(1,1), (-4,1), (-4,-2), (-2,-2), (1,-1)],
			"rr":[(1,1), (-2,1), (-2,-1), (-1,-4), (1,-4)],
			"rrr":[(1,1), (-1,1), (-4,0), (-4,-2), (1,-2)],
			"f":[(1,1), (-1,1), (-2,-2), (-2,-4), (1,-4)],
			"fr":[(1,0), (-2,1), (-4,1), (-4,-2), (1,-2)],
			"frr":[(1,1), (-2,1), (-2,-4), (0,-4), (1,-1)],
			"frrr":[(1,1), (-4,1), (-4,-1), (-1,-2), (1,-2)]}
		elif self.name == "LONG_T":
			self.legal_moves = {
			"":[(1,0), (-1,1), (-3,1), (-3,-3), (-1,-3), (1,-2)],
			"r":[(1,1), (-3,1), (-3,-1), (-2,-3), (0,-3), (1,-1)],
			"rr":[(1,1), (-1,1), (-3,0), (-3,-2), (-1,-3), (1,-3)],
			"rrr":[(1,-1), (0,1), (-2,1), (-3,-1), (-3,-3), (1,-3)]}
		elif self.name == "LONG_CORNER":
			self.legal_moves = {
			"":[(1,1), (-1,1), (1,-3), (-3,-3), (-3,-1)],
			"r":[(1,-1), (-1,1), (-3,1), (-3,-3), (1,-3)],
			"rr":[(1,1), (-3,1), (-3,-3), (-1,-3), (1,-1)],
			"rrr":[(1,1), (-3,1), (-3,-1), (-1,-3), (1,-3)]}
		elif self.name == "RIFLE":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-2,-2), (-1,-4), (1, -4)],
			"r":[(1,1), (-2,1), (-4,0), (-4,-2), (0,-2), (1, -1)],
			"rr":[(0,1), (-2,1), (-2,-3), (-1,-4), (1,-4), (1, -1)],
			"rrr":[(1,1), (-3,1), (-4,0), (-4,-2), (-1,-2), (1, -1)],
			"f":[(1,1), (-1,1), (-2,0), (-2,-4), (0,-4), (1, -2)],
			"fr":[(1,0), (0,1), (-4,1), (-4,-1), (-2,-2), (1, -2)],
			"frr":[(1,1), (-1,1), (-2,-1), (-2,-4), (0,-4), (1, -3)],
			"frrr":[(1,0), (-1,1), (-4,1), (-4,-1), (-3,-2), (1, -2)]}
		elif self.name == "Z":
			self.legal_moves = {
			"":[(1,-1), (0,1), (-3,1), (-3,-1), (-2,-3), (1, -3)],
			"r":[(1,1), (-1,1), (-3,0), (-3,-3), (-1,-3), (1, -2)],
			"f":[(1,1), (-2,1), (-3,-1), (-3,-3), (0,-3), (1, -1)],
			"fr":[(1,0), (-1,1), (-3,1), (-3,-2), (-1,-3), (1, -3)]}			
		elif self.name == "UTAH":
			self.legal_moves = {
			"":[(1,1), (-3,1), (-3,-2), (0,-2), (1,-1)],
			"r":[(1,1), (-2,1), (-2,-2), (-1,-3), (1,-3)],
			"rr":[(1,1), (-2,1), (-3,0), (-3,-2), (1,-2)],
			"rrr":[(1,0), (0,1), (-2,1), (-2,-3), (1,-3)],
			"f":[(1,1), (-3,1), (-3,-1), (-2,-2), (1,-2)],
			"fr":[(1,1), (-1,1), (-2,0), (-2,-3), (1,-3)],
			"frr":[(1,0), (0,1), (-3,1), (-3,-2), (1,-2)],
			"frrr":[(1,1), (-2,1), (-2,-3), (0,-3), (1,-2)]}
		elif self.name == "W":
			self.legal_moves = {
			"":[(0,1), (-3,1), (-3,-1), (-2,-2), (-1,-3), (1,-3), (1,0)],
			"r":[(1,1), (-1,1), (-2,0), (-3,-1), (-3,-3), (0,-3), (1,-2)],
			"rr":[(1,-1), (0,0), (-1,1), (-3,1), (-3,-2), (-2,-3), (1,-3)],
			"rrr":[(1,1), (-2,1), (-3,0), (-3,-3), (-1,-3), (0,-2), (1,-1)]}
		elif self.name == "U":
		 	self.legal_moves = {
			"":[(1,1), (-3,1), (-3,-2), (-1,-2), (1,-2)],
			"r":[(1,1), (-2,1), (-2,1), (-2,-3), (1,-3)],
			"rr":[(1,1), (-1,1), (-3,1), (-3,-2), (1,-2)],
			"rrr":[(1,1), (-2,1), (-2,-3), (1,-3), (1,-1)]}
		elif self.name == "F":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-3,0), (-3,-2), (-1,-3), (1, -3)],
			"r":[(1,0), (0,1), (-2,1), (-3,-1), (-3,-3), (0,-3), (1,-2)],
			"rr":[(1,0), (-1,1), (-3,1), (-3,-2), (-2,-3), (0,-3), (1, -2)],
			"rrr":[(1,1), (-2,1), (-3,0), (-3,-2), (-2,-3), (0,-3), (1,-1)],
			"f":[(1,0), (0,1), (-2,1), (-3,0), (-3,-3), (-1,-3), (1,-2)],
			"fr":[(1,0), (0,1), (-3,1), (-3,-1), (-2,-3), (0,-3), (1,-2)],
			"frr":[(1,1), (-1,1), (-3,0), (-3,-2), (-2,-3), (0,-3), (1, -2)],
			"frrr":[(1,-1), (0,1), (-2,1), (-3, 0), (-3,-2), (-2,-3), (1,-3)]}
		elif self.name == "CROSS":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-3,0), (-3,-2), (-2,-3), (0,-3), (1,-2)]}
		elif self.name == "BIRD":
			self.legal_moves = {
			"":[(1,0), (0,1), (-2,1), (-2,-4), (0,-4), (1,-2)],
			"r":[(1,1), (-4,1), (-4,-1), (-2,-2), (0,-2), (1,-1)],
			"rr":[(1,1), (-1,1), (-2,-1), (-2,-3), (-1,-4), (1,-4)],
			"rrr":[(1,0), (-1,1), (-3,1), (-4,0), (-4,-2), (1,-2)],
			"f":[(1,1), (-1,1), (-2,0), (-2,-2), (-1,-4), (1,-4)],
			"fr":[(1,0), (0,1), (-2,1), (-4,0), (-4,-2), (1,-2)],
			"frr":[(1,-1), (0,1), (-2,1), (-2,-4), (0,-4), (1,-3)],
			"frrr":[(1,1), (-4,1), (-4,-1), (-3,-2), (-1,-2), (1,-1)]}
		


	def reset(self):
		self.set_shape()

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

	def get_legal_moves(self):
		return self.legal_moves


