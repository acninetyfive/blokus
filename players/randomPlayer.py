import random
from players.computerPlayer import ComputerPlayer

class RandomPlayer(ComputerPlayer):
	
	def __init__(self, name, color):
		super().__init__(name, color)

	def get_name(self):
		return super().get_name()

	def get_pieces(self):
		return super().get_pieces()

	def del_piece(self, p):
		super().del_piece(p)

	def get_score(self):
		return super().get_score()

	def get_type(self):
		return super().get_type()

	#return a move to be played as a tuple: (piece, flip/rotation string, (x, y))
	def get_move(self, board):
		return random.choice(board.get_moves_list(self, board.get_color_corners(self.color)))
