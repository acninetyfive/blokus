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
		self.c = [[1,0,1],[0,0,0],[1,0,1]]
		self.a = [[0,1,0],[1,1,1],[0,1,0]]	

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
			#print("Piece off the edge of the board")
			return False
		if len(np.nonzero(self.board[x:x+px,y:y+py] * piece.get_shape())[0]) > 0: #Piece on top of another piece
			#print("Piece on top of another")
			return False
		for i in self.generate_adjacents(shape_coords): #Piece adjacent to same color
			if i[0] < self.size and i[0] >= 0 and i[1] < self.size and i[1] >= 0 and self.board[i] == p_color:
				#print("piece adjacent to the same color")
				return False
		for i in self.generate_corners(shape_coords): #Piece is touching a corner
			if i[0] < self.size and i[0] >= 0 and i[1] < self.size and i[1] >= 0 and self.board[i] == p_color:
				return True
		for x in shape_coords:
			if list(x) in self.start_squares:
				return True
		#print("else")
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
	
	def get_color_corners(self, color): 
		one_color_board = np.array(self.board == color, dtype="int") * color
		corner_board = convolve(one_color_board, self.c, mode='constant') - 20 * convolve(one_color_board, self.a, mode='constant') - 20 * self.board
		return np.array(np.where(corner_board >= 1))

	def get_moves_list(self, player, corners):
		playable_moves = []
		pcs = player.get_pieces()
		if len(pcs) == 21: 
			start_squares = np.array([[0,0,19,19],[0,19,0,19]])
			corners = np.hstack((corners, start_squares))
		for p in pcs:
			moves = pcs[p].get_legal_moves()
			pcs[p].reset()
			for m in moves:
				for c in m:
					if c == 'r':
						pcs[p].rotate()
					elif c == 'f':
						pcs[p].flip()
				for i in moves[m]:
					shp = pcs[p].get_shape()
					for j in range(len(corners[0])):
						x = corners[0,j]+i[0]
						y = corners[1,j]+i[1]
						if x < 0 or x > self.size - 1:
							pass
						elif y < 0 or y > self.size - 1:
							pass
						elif self.valid_move(pcs[p],x,y):
							playable_moves.append((p, m, x, y))

				pcs[p].reset()
		return playable_moves

	def get_board(self):
		return self.board

