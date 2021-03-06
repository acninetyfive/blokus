import pygame
import sys
import importlib
from board import Board
from piece import Piece

# Import players
if not (len(sys.argv) == 1 or len(sys.argv) == 9):
    print("Please specify either 4 or 0 players!")
    exit(1)
if len(sys.argv) == 1:
    RandomPlayer = importlib.import_module("players.randomPlayer").Player
    player_list = [RandomPlayer("Gabe", 1), RandomPlayer("Kevin", 2), RandomPlayer("Alissa", 3), RandomPlayer("John V", 4)]
else:
    player_list = []
    for i, color in zip(range(1, 9, 2), range(1, 5)):
        Player = importlib.import_module(f"players.{sys.argv[i + 1]}").Player
        player_list.append(Player(sys.argv[i], color))


# Define some colors
BLACK = (0, 0, 0)
GRAY = (200,200,200)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Colors for each player
color_dict = {
                1 : BLUE,
                2 : GREEN,
                3 : RED,
                4 : YELLOW
            }
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 3

# This sets the number of cells (size x size)
size = 20


background = pygame.rect.Rect(0, 0, (HEIGHT + MARGIN) * size + MARGIN, (WIDTH + MARGIN) * size + MARGIN)
 
# Initialize pygame
pygame.init()
 
# Set the WIDTH and HEIGHT of the screen
WINDOW_SIZE = [(HEIGHT + MARGIN) * size + MARGIN  + 250, (WIDTH + MARGIN) * size + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("¡Blokus!")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

finished_players = []
game_board = Board(size, [1,2,3,4])

turn_one = [True, True, True, True]
active_player = 0
available_pieces = player_list[active_player].get_pieces()
p_num = 0
active_piece = available_pieces[list(available_pieces)[p_num]]


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

def draw_piece(piece, x, y):
    piece_shape = piece.get_shape()
    px, py = piece_shape.shape
    for row in range(px):
        for column in range(py):
            color = WHITE
            if piece_shape[row][column] != 0:
                color = color_dict[piece_shape[row][column]]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + x,
                              (MARGIN + HEIGHT) * row + y,
                              WIDTH,
                              HEIGHT])

def pass_turn(a_p):
    if turn_one[a_p]:
        turn_one[a_p] = False
    n_p = (a_p + 1) % len(player_list)
    next_player = player_list[n_p]
    cnrs = game_board.get_color_corners(next_player.get_color())
    print("Player " + str(player_list[a_p].get_color()) + "'s score is " + str(player_list[a_p].get_score()))
    print("Passing to player ", next_player.get_color())
    print("finished_players", finished_players)
    print()
    tp = Piece(next_player.get_color(), 'ONE')
    mvs = game_board.get_moves_list(next_player, cnrs)
    if not turn_one[n_p]:
        if len(mvs) == 0:
            print("Player " + str(n_p) + " is finished")
            finished_players.append(player_list[n_p])
            if len(finished_players) == len(player_list):
                return None
            return pass_turn(n_p)
    for x in mvs:
        print(x)

    return n_p

def handle_event(event, done, p_num, active_piece, active_player):

    available_pieces = player_list[active_player].get_pieces()

    if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    elif event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)

        if active_piece:
            if game_board.add_piece(active_piece, row, column):
                player_list[active_player].del_piece(active_piece.get_name())
                available_pieces = player_list[active_player].get_pieces()
                if len(available_pieces) == 0:
                    active_piece = None
                    finished_players.append(active_player)
                active_player = pass_turn(active_player)
                if active_player == None:
                    done = True
                    return done, active_piece, active_player
                available_pieces = player_list[active_player].get_pieces()
                p_num = 0
                active_piece = available_pieces[list(available_pieces)[p_num]]

        #print("Click ", pos, "Grid coordinates: ", row, column)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            active_piece.rotate()
        if event.key == pygame.K_f:
            active_piece.flip()
        if event.key == pygame.K_RIGHT:
            p_num = (p_num + 1) % len(available_pieces)
            active_piece.reset()
            active_piece = available_pieces[list(available_pieces)[p_num]]
        if event.key == pygame.K_LEFT:
            p_num = (p_num - 1) % len(available_pieces)
            active_piece.reset()
            active_piece = available_pieces[list(available_pieces)[p_num]]

    '''elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:            
            if rectangle.collidepoint(event.pos):
                rectangle_draging = True
                mouse_x, mouse_y = event.pos
                offset_x = rectangle.x - mouse_x
                offset_y = rectangle.y - mouse_y

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:            
            rectangle_draging = False

    elif event.type == pygame.MOUSEMOTION:
        if rectangle_draging:
            mouse_x, mouse_y = event.pos
            rectangle.x = mouse_x + offset_x
            rectangle.y = mouse_y + offset_y'''

    return done, p_num, active_piece, active_player

def draw_screen():
    # Set the screen background
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, background)

    # Draw the grid
    grid = game_board.get_board()
    for row in range(size):
        for column in range(size):
            color = GRAY
            if grid[row][column] != 0:
                color = color_dict[grid[row][column]]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    if active_piece != None:
        draw_piece(active_piece, (HEIGHT + MARGIN) * size + MARGIN  + 80, 100)

    if active_player != None:
        current_name = player_list[active_player].get_name()
        message_display(current_name, (HEIGHT + MARGIN) * size + MARGIN  + 125, 50, 25)    

    pygame.display.flip()

    return 1


# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:

    player_type = player_list[active_player].get_type()

    if player_type == "human":
        for event in pygame.event.get():  # User did something
            done, p_num, active_piece, active_player = handle_event(event, done, p_num, active_piece, active_player)
    else:
        move = player_list[active_player].get_move(game_board)
        piece = player_list[active_player].get_pieces()[move[0]]
        piece.reset()
        for c in move[1]:
            if c == 'r':
                piece.rotate()
            elif c == 'f':
                piece.flip()
        print("move")
        print(move)
        if game_board.add_piece(piece, move[2], move[3]):
            player_list[active_player].del_piece(piece.get_name())
            available_pieces = player_list[active_player].get_pieces()
            if len(available_pieces) == 0:
                active_piece = None
                finished_players.append(active_player)
            active_player = pass_turn(active_player)
            if active_player == None:
                    done = True
            else:
                available_pieces = player_list[active_player].get_pieces()
                p_num = 0
                active_piece = available_pieces[list(available_pieces)[p_num]]

    draw_screen()
 
    # Limit to 60 frames per second
    clock.tick(60)


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
#pygame.display.quit()
print("quit")
input()
pygame.quit()

scores = [(p.get_name(), p.get_score()) for p in player_list]
scores = sorted(scores, key=lambda x: x[1])
for x in scores:
    print(x[0], "scored", x[1])
print(scores[0][0], "won!")

 


