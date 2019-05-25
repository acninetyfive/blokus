from players.randomPlayer import RandomPlayer
from players.humanPlayer import HumanPlayer
from board import Board
from piece import Piece
import time
import sys

if len(sys.argv) > 1:
	runs = int(sys.argv[1])
else:
	runs = 100

r = RandomPlayer("randy", 1)
b = Board()

b.board[7,7] = 1

#print("board", b.board)
#print()
#print("corners", b.get_color_corners(1))

example_board = Board()
example_board.board[7,7] = 2

def reset_example():
	example_board = Board()


s = time.perf_counter()

for _ in range(runs):
	b.get_moves_list(r, b.get_color_corners(r.get_color()))

t = time.perf_counter()

print("Get moves list")
print("runs", runs)
print("time", t-s)
print("time per run", (t-s)/runs)
print()


valid_count = 0
invalid_count = 0

s = time.perf_counter()
for _ in range(runs):
	move = r.get_move(b)
	piece = r.get_pieces()[move[0]]
	piece.reset()
	shp = piece.get_shape()
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
		print(move)
		print("invalid!!!")
		print("initial shape")
		print (shp)
		print("final shape") 
		print(piece.get_shape())
		p_shape = piece.get_shape()
		px, py = p_shape.shape
		example_board.board[move[2][0]:move[2][0] + px, move[2][1]:move[2][1]+py] += p_shape
		example_board.board[7,7] += 2
		print(example_board.board)
		input()
		reset_example()
		invalid_count += 1

t = time.perf_counter()
print("Get move from random player")
print("valid", valid_count)
print("invalid", invalid_count)
print("runs", runs)
print("time", t-s)
print("time per run", (t-s)/runs)

print("Done")