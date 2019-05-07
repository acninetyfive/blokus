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
		for p in self.pieces:
			print(self.pieces[p].get_name())
			print(self.pieces[p].get_shape())
			print()