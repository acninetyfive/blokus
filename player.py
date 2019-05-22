import numpy as np
from piece import Piece

class Player:

	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.pieces = {t:Piece(color, t) for t in [
			'ONE', 'TWO', 'THREE', 'FOUR', "FIVE",
			'SHORT_CORNER', 'SQUARE', 'SHORT_T', 'SHORT_L',
			'S', 'LONG_L', 'LONG_T', 'LONG_CORNER', 'RIFLE',
			'Z', 'UTAH', 'W', 'U', 'F', 'CROSS', 'BIRD'
			]}

	def get_name(self):
		return self.name

	def get_color(self):
		return self.color

	def get_pieces(self):
		return self.pieces

	def del_piece(self, p):
		if p in self.pieces:
			del self.pieces[p]

	def get_score(self):
		score = 0
		for p in self.pieces:
			score += self.pieces[p].get_value()
		return score
