import numpy as np
from piece import Piece
import time

class Trie:
	def __init__(self):
		self.root = TrieNode("root", None)

	def get_root(self):
		return self.root

	def add_node(self, points, value):
		p = 0
		node = self.root
		while points[p] in node.get_children():
			node = node.get_children()[points[p]]
			p += 1
			if p == len(points):
				node.set_value(value)
				return node
		while p < len(points) - 1:
			node = node.add_child(None, points[p])
			p += 1
		node.add_child(value, points[p])
		return node



class TrieNode:
	def __init__(self, value, point):
		self.value = value
		self.point = point
		self.children = {}

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_point(self):
		return self.point

	def get_children(self):
		return self.children

	def add_child(self, value, point):
		self.children[point] = TrieNode(value, point)
		return self.children[point]



def get_points_from_shape(shape, start):
	if shape[start] == 0: #not valid starting spot
		return None
	start = tuple(start)
	visited = []
	stack = [start]

	while stack:
		cur = stack.pop()
		visited.append(cur)

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

	relative_visited = [(x[0] - start[0], x[1] - start[1]) for x in visited] #list each visited node's coordinates relative to the "corner" spot

	return relative_visited


def trie_dfs(trie):
	root = trie.get_root()
	visited = []
	stack = [root]

	while stack:
		node = stack.pop()
		visited.append(node)
		children = node.get_children()
		for n in children:
			stack.append(children[n])

	return visited

def trie_bfs(trie):
	root = trie.get_root()
	visited = []
	queue = [root]

	while queue:
		node = queue.pop(0)
		visited.append(node)
		children = node.get_children()
		for n in children:
			queue.append(children[n])

	return visited
	

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
				d[pname][m][pos] = get_points_from_shape(pieces[p].get_shape(), (pos[0] * -1, pos[1] * -1))
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
	trie = Trie()
	for key in pts_dict:
		trie.add_node(key, pts_dict[key])
	return trie

	
pieces = {t:Piece(1, t) for t in [
			'ONE', 'TWO', 'THREE', 'FOUR', "FIVE",
			'SHORT_CORNER', 'SQUARE', 'SHORT_T', 'SHORT_L',
			'S', 'LONG_L', 'LONG_T', 'LONG_CORNER', 'RIFLE',
			'Z', 'UTAH', 'W', 'U', 'F', 'CROSS', 'BIRD'
			]}

piece_to_points_dict = build_piece_to_points_dict(pieces)

points_to_piece_dict = build_points_to_piece_dict(piece_to_points_dict)

my_trie = trie_from_dict(points_to_piece_dict)

nodes_list = trie_bfs(my_trie)

for n in nodes_list:
	print(n.get_point(), n.get_value())

