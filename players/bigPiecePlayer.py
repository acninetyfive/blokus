import random
from players.computerPlayer import ComputerPlayer

class Player(ComputerPlayer):
	
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
		mvs = board.get_moves_list(self, board.get_color_corners(self.color))
		mv_dict = self.sort_moves(mvs)
		x = 5
		while x > 0:
			if len(mv_dict[x]) > 0:
				return random.choice(mv_dict[x])
			x -= 1
		return None

	def sort_moves(self, moves):
		mv_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
		for m in moves:
			mv_dict[self.pieces[m[0]].get_value()].append(m)
		return mv_dict
