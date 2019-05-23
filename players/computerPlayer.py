from players.basePlayer import BasePlayer

class ComputerPlayer(BasePlayer):
	
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
		return "human"

	#return a move to be played as a tuple: (piece, flip/rotation string, (x, y))
	def get_move(self, board):
		pass