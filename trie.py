import numpy as np
from piece import Piece
import time

class Trie:
    def __init__(self):
        self.root = TrieNode("root", None)

    def get_root(self):
        return self.root

    def add_node(self, points, piece):
        p = 0
        node = self.root
        while points[p] in node.get_children():
            node = node.get_children()[points[p]]
            p += 1
            if p == len(points):
                node.set_piece(piece)
                return node
        while p < len(points) - 1:
            node = node.add_child(None, points[p])
            p += 1
        node.add_child(piece, points[p])
        return node


class TrieNode:
    def __init__(self, piece, point):
        self.piece = piece
        self.point = point
        self.children = {}

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_point(self):
        return self.point

    def get_children(self):
        return self.children

    def add_child(self, piece, point):
        self.children[point] = TrieNode(piece, point)
        return self.children[point]


class TrieBuilder:
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


    def trie_from_dict(points_to_piece_dict):
        trie = Trie()
        for key in points_to_piece_dict:
            trie.add_node(key, points_to_piece_dict[key])
        return trie



