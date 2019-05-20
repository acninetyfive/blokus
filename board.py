import numpy as np
from piece import Piece
import time
from scipy.ndimage import convolve

class Board:

	def __init__(self, size = 20, player_colors = [1,2,3,4]):
		self.size = size
		self.board = np.zeros((size,size), dtype = int)
		self.start_squares = [[0,0], [0, size-1], [size-1, 0], [size-1, size-1]]
		self.player_colors = player_colors
		self.corners_and_adjacents = np.zeros((size,size), dtype = int)
		self.corners_and_adjacents[[0,0,size-1,size-1],[0,size-1,0,size-1]] = [1,2,3,4]	
		self.c = [[1,0,1],[0,0,0],[1,0,1]]
		self.a = [[0,1,0],[1,0,1],[0,1,0]]	

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
		if len(np.nonzero(self.board[x:x+px,y:y+py] * piece.get_shape())[0]) > 0: #Piece on top of another piece
			return False
		for i in self.generate_adjacents(shape_coords): #Piece adjacent to same color
			if i[0] < self.size and i[0] >= 0 and i[1] < self.size and i[1] >= 0 and self.board[i] == p_color:
				return False
		for i in self.generate_corners(shape_coords): #Piece is touching a corner
			if i[0] < self.size and i[0] >= 0 and i[1] < self.size and i[1] >= 0 and self.board[i] == p_color:
				return True
		for x in shape_coords:
			if list(x) in self.start_squares:
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

		#print(corners - self.generate_adjacents(shape_coords)) #true corners
		return corners

	def get_board(self):
		return self.board

	def c_v(self):
		convolve(self.board, self.a, mode = 'constant')
		convolve(self.board, self.c, mode = 'constant')
		return

	def generate_kernel(self, piece):
		cnr = np.array([[1,0,1],[0,0,0],[1,0,1]])
		adj = np.array([[0,1,0],[1,0,1],[0,1,0]])

		p_shape = piece.get_shape()
		px, py = p_shape.shape
		embed_arr = np.zeros((px + 2, py + 2))
		embed_arr[1:px + 1, 1:py + 1] = p_shape

		p_a = convolve(embed_arr, adj, mode = 'constant')
		p_c = convolve(embed_arr, cnr, mode = 'constant')

		p_c[p_a > 0] = -10

		kernel = np.flip(p_c, 0)
		kernel = np.flip(kernel, 1)

		return kernel

