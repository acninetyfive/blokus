from player import Player
from board import Board
from piece import Piece

g = Player("g", 1)
b = Board()
pcs = g.get_pieces()

b.board[7,7] = 1


'''
for p in pcs:
	moves = pcs[p].get_legal_moves()
	for m in moves:
		pcs[p].reset()
		for c in m:
			if c == 'r':
				pcs[p].rotate()
			elif c == 'f':
				pcs[p].flip()
		for i in moves[m]:
			if b.valid_move(pcs[p],7+i[0],7+i[1]):
				print (p, m, i)
				print(pcs[p].get_shape())
'''

for p in pcs:
	print(p)
	print(pcs[p].get_shape())
	print(pcs[p].get_value())
	print()

print("Done")
