import numpy as np
from piece import Piece
import time

class TrieNode:

	def __init__(self, value):
		self.value = ("piece", "orientation", "move")
		self.point = ("x", "y")
		self.children = []



def dfs(shape, start):
	if shape[start] == 0:
		return None
	start = tuple(start)
	visited = []
	stack = [start]
	#print(shape)

	while stack:
		cur = stack.pop()
		visited.append(cur)
		#print(cur)
		if cur[0] > 0:
			if shape[cur[0] - 1, cur[1]] != 0 and (cur[0] - 1, cur[1]) not in visited and (cur[0] - 1, cur[1]) not in stack:
				stack.append((cur[0] - 1, cur[1]))
		if cur[1] > 0:
			if shape[cur[0], cur[1] - 1] != 0 and (cur[0], cur[1] - 1) not in visited and (cur[0], cur[1] - 1) not in stack:
				stack.append((cur[0], cur[1] - 1))
		if cur[0] < len(shape) - 1:
			if shape[cur[0] + 1, cur[1]] != 0 and (cur[0] + 1, cur[1]) not in visited and (cur[0] + 1, cur[1]) not in stack:
				stack.append((cur[0] + 1, cur[1]))
		if cur[1] < len(shape[0]) - 1:
			if shape[cur[0], cur[1] + 1] != 0 and (cur[0], cur[1] + 1) not in visited and (cur[0], cur[1] + 1) not in stack:
				stack.append((cur[0], cur[1] + 1))
		#print("visited", visited)
		#print("stack", stack)
		#print()


	relative_visited = [(x[0] - start[0], x[1] - start[1]) for x in visited] #list each visited node's coordinates relative to the "corner" spot

	return relative_visited
	

def build_piece_to_points_dict(pieces):
	d = {}
	for p in pieces:
		pname = p
		d[pname] = {}
		mvs = pieces[p].get_legal_moves()
		for m in mvs:
			d[pname][m] = {}
			for c in m:
				if c == 'r':
					pieces[p].rotate()
				elif c == 'f':
					pieces[p].flip()
			for pos in mvs[m]:
				d[pname][m][pos] = dfs(pieces[p].get_shape(), (pos[0] * -1, pos[1] * -1))
			pieces[p].reset()
	return d


def build_points_to_piece_dict(pc_to_pts):
	d = {}
	for p in pc_to_pts:
		for orient in pc_to_pts[p]:
			for mv in pc_to_pts[p][orient]:
				 d[tuple(pc_to_pts[p][orient][mv])] = (p, orient, mv)
	return d


def trie_from_dict(pts_dict):
	pass


t = time.perf_counter()
pieces = {t:Piece(1, t) for t in [
			'ONE', 'TWO', 'THREE', 'FOUR', "FIVE",
			'SHORT_CORNER', 'SQUARE', 'SHORT_T', 'SHORT_L',
			'S', 'LONG_L', 'LONG_T', 'LONG_CORNER', 'RIFLE',
			'Z', 'UTAH', 'W', 'U', 'F', 'CROSS', 'BIRD'
			]}

piece_to_points_dict = build_piece_to_points_dict(pieces)

points_to_piece_dict = build_points_to_piece_dict(piece_to_points_dict)

print(time.perf_counter() - t)

for k in sorted(points_to_piece_dict, key=len):
	print(k, points_to_piece_dict[k])


