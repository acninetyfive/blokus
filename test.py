from players.randomPlayer import RandomPlayer
from board import Board
from piece import Piece

r = RandomPlayer("randy", 1)
b = Board()

b.board[7,7] = 1

#print(b.get_board())

valid_count = 0
invalid_count = 0

test_moves = b.get_moves_list(r, b.get_color_corners(r.get_color()))
for move in test_moves:
	piece = r.get_pieces()[move[0]]
	piece.reset()
	for c in move[1]:
		if c == 'r':
			piece.rotate()
		elif c == 'f':
			piece.flip()
		if b.valid_move(piece,move[2][0],move[2][1]):
			#print (move)
			#print("valid")
			#print()
			valid_count += 1
		else:
			print (move)
			print("invalid!!!")
			print(piece.get_shape())
			print()
			invalid_count += 1

print("valid", valid_count)
print("invalid", invalid_count)
'''

for p in pcs:
	print(p)
	print(pcs[p].get_shape())
	print(pcs[p].get_value())
	print()

print("Done")

'''
