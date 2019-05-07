import numpy as np
import piece

class Board:

	def __init__(self, size = 20):
		self.size = size
		self.board = np.zeros((size,size), dtype = int)
		self.valid_squares = np.array([[[0,0]], [[0, size-1]], [[size-1, 0]], [[size-1, size-1]]])

	def add_piece(self, piece, x, y):
		if not self.valid_move(piece, x, y):
			return False
		p_shape = piece.get_shape()
		px, py = p_shape.shape
		self.board[x:x + px, y:y+py] += p_shape
		return True

	def valid_move(self, piece, x, y):
		p_shape = piece.get_shape()
		p_color = piece.get_color()
		px, py = p_shape.shape
		shape_coords = np.argwhere(p_shape != 0) + [x,y]
		if x + px > self.size or y + py > self.size: #Piece off the edge of the board
			return False
		if np.any(self.board[x:x+px,y:y+py] & piece.get_shape()): #Piece on top of another piece
			return False
		for i in self.generate_adjacents(shape_coords): #Piece adjacent to same color
			if i[0] < self.size and i[1] < self.size and self.board[i] == p_color:
				return False
		for i in self.generate_corners(shape_coords): #Piece is touching a corner
			if i[0] < self.size and i[1] < self.size and self.board[i] == p_color:
				return True
		return False

	def generate_adjacents(self, shape_coords):
		adj = set()
		for i in shape_coords:
			adj.add((i[0] + 1, i[1]))
			adj.add((i[0], i[1] + 1))
			adj.add((i[0] - 1, i[1]))
			adj.add((i[0], i[1] - 1))
		return adj

	def generate_corners(self, shape_coords):
		corners = set()
		for i in shape_coords:
			corners.add((i[0] + 1, i[1] + 1))
			corners.add((i[0] - 1, i[1] + 1))
			corners.add((i[0] + 1, i[1] - 1))
			corners.add((i[0] - 1, i[1] - 1))
		return corners