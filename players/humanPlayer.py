from players.basePlayer import BasePlayer

class HumanPlayer(BasePlayer):
	
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