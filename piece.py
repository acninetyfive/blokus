from enum import Enum
import numpy as np
from scipy.ndimage import convolve

class Piece:

    def __init__(self, color, name): 
        self.color = color
        self.name = name
        self.set_shape()
        self.set_legal_moves()
        self.value = np.sum(self.shape > 0)
        

    def set_shape(self):
        if self.name == "ONE":
            self.shape = np.array([[1]]) * self.color
        elif self.name == "TWO":
            self.shape = np.array([[1,1]]) * self.color
        elif self.name == "THREE":
            self.shape = np.array([[1,1,1]]) * self.color
        elif self.name == "FOUR":
            self.shape = np.array([[1,1,1,1]]) * self.color
        elif self.name == "FIVE":
            self.shape = np.array([[1,1,1,1,1]]) * self.color
        elif self.name == "SHORT_CORNER":
            self.shape = np.array([[1,1], [0,1]]) * self.color
        elif self.name == "SQUARE":
            self.shape = np.array([[1,1], [1,1]]) * self.color
        elif self.name == "SHORT_T":
            self.shape = np.array([[0,1,0], [1,1,1]]) * self.color
        elif self.name == "SHORT_L":
            self.shape = np.array([[0,0,1], [1,1,1]]) * self.color
        elif self.name == "S":
            self.shape = np.array([[0,1,1], [1,1,0]]) * self.color
        elif self.name == "LONG_L":
            self.shape = np.array([[0,0,0,1], [1,1,1,1]]) * self.color
        elif self.name == "LONG_T":
            self.shape = np.array([[0,1,0], [0,1,0], [1,1,1]]) * self.color
        elif self.name == "LONG_CORNER":
            self.shape = np.array([[1,1,1], [0,0,1], [0,0,1] ]) * self.color
        elif self.name == "RIFLE":
            self.shape = np.array([[0,1,1,1], [1,1,0,0]]) * self.color
        elif self.name == "Z":
            self.shape = np.array([[0,0,1], [1,1,1], [1,0,0]]) * self.color 
        elif self.name == "UTAH":
            self.shape = np.array([[1,0], [1,1], [1,1]]) * self.color
        elif self.name == "W":
            self.shape = np.array([[0,1,1], [1,1,0], [1,0,0]]) * self.color 
        elif self.name == "U":
            self.shape = np.array([[1,1], [1,0], [1,1]]) * self.color 
        elif self.name == "F":
            self.shape = np.array([[0,1,1], [1,1,0], [0,1,0]]) * self.color
        elif self.name == "CROSS":
            self.shape = np.array([[0,1,0], [1,1,1], [0,1,0]]) * self.color
        elif self.name == "BIRD":
            self.shape = np.array([[0,1,0,0], [1,1,1,1]]) * self.color
        
        
    def set_legal_moves(self):
        if self.name == "ONE": 
            self.legal_moves = {
            "":[]} 
        elif self.name == "TWO": 
            self.legal_moves = {
            "":[],
            "r":[]}
        elif self.name == "THREE":
            self.legal_moves = {
            "":[],
            "r":[]}
        elif self.name == "FOUR":
            self.legal_moves = {
            "":[],
            "r":[]}
        elif self.name == "FIVE":
            self.legal_moves = {
            "":[],
            "r":[]}
        elif self.name == "SHORT_CORNER":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "SQUARE":
            self.legal_moves = {
            "":[]}
        elif self.name == "SHORT_T":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "SHORT_L":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}
        elif self.name == "S":
            self.legal_moves = {
            "":[],
            "r":[],
            "f":[],
            "fr":[]}
        elif self.name == "LONG_L":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}
        elif self.name == "LONG_T":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "LONG_CORNER":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "RIFLE":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}
        elif self.name == "Z":
            self.legal_moves = {
            "":[],
            "r":[],
            "f":[],
            "fr":[]}            
        elif self.name == "UTAH":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}
        elif self.name == "W":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "U":
             self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[]}
        elif self.name == "F":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}
        elif self.name == "CROSS":
            self.legal_moves = {
            "":[]}
        elif self.name == "BIRD":
            self.legal_moves = {
            "":[],
            "r":[],
            "rr":[],
            "rrr":[],
            "f":[],
            "fr":[],
            "frr":[],
            "frrr":[]}

        ne_kernel = [[0,-10,0], [0,1,-10], [0,0,0]]
        se_kernel = [[0,0,0], [0,1,-10], [0,-10,0]]
        sw_kernel = [[0,0, 0], [-10,1,0], [0,-10,0]]
        nw_kernel = [[0,-10, 0], [-10,1,0], [0,0,0]]

        for s in self.legal_moves:
            for c in s:
                if c == 'r':
                    self.rotate()
                elif c == 'f':
                    self.flip()

            ne_conv = convolve(self.get_shape(), ne_kernel, mode = 'constant')
            se_conv = convolve(self.get_shape(), se_kernel, mode = 'constant')
            sw_conv = convolve(self.get_shape(), sw_kernel, mode = 'constant')
            nw_conv = convolve(self.get_shape(), nw_kernel, mode = 'constant')

            ne_bool = ne_conv > 0
            se_bool = se_conv > 0
            sw_bool = sw_conv > 0
            nw_bool = nw_conv > 0

            final = ne_bool + se_bool + sw_bool + nw_bool
            self.legal_moves[s] = [(x[0], x[1]) for x in np.transpose(np.array(np.where(final)) * -1)]
            self.reset()

            
    def reset(self):
        self.set_shape()

        
    def rotate(self):
        self.shape = np.array(list(zip(*self.shape[::-1])))

        
    def flip(self):
        self.shape = np.flip(self.shape, 0)


    def get_points_from_shape(self, start):
        if self.shape[start] == 0: #not valid starting spot
            return None
        start = tuple(start)
        visited = []
        stack = [start]

        while stack:
            cur = stack.pop()
            visited.append(cur)

            if cur[0] > 0:
                if self.shape[cur[0] - 1, cur[1]] != 0 and (cur[0] - 1, cur[1]) not in visited and (cur[0] - 1, cur[1]) not in stack:
                    stack.append((cur[0] - 1, cur[1]))
            if cur[1] > 0:
                if self.shape[cur[0], cur[1] - 1] != 0 and (cur[0], cur[1] - 1) not in visited and (cur[0], cur[1] - 1) not in stack:
                    stack.append((cur[0], cur[1] - 1))
            if cur[0] < len(shape) - 1:
                if self.shape[cur[0] + 1, cur[1]] != 0 and (cur[0] + 1, cur[1]) not in visited and (cur[0] + 1, cur[1]) not in stack:
                    stack.append((cur[0] + 1, cur[1]))
            if cur[1] < len(self.shape[0]) - 1:
                if self.shape[cur[0], cur[1] + 1] != 0 and (cur[0], cur[1] + 1) not in visited and (cur[0], cur[1] + 1) not in stack:
                    stack.append((cur[0], cur[1] + 1))

        relative_visited = [(x[0] - start[0], x[1] - start[1]) for x in visited] #list each visited node's coordinates relative to the "corner" spot

        return relative_visited

        
    def get_shape(self):
        return self.shape

    
    def get_color(self):
        return self.color

    
    def get_name(self):
        return self.name

    
    def get_legal_moves(self):
        return self.legal_moves

    
    def get_value(self): 
        return self.value
