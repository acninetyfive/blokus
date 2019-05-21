import pygame
from board import Board
from piece import Piece
from player import Player

#rectangle = pygame.rect.Rect(176, 134, 17, 17)
#rectangle_draging = False

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
 
size = 20


background = pygame.rect.Rect(0, 0, (HEIGHT + MARGIN) * size + MARGIN, (WIDTH + MARGIN) * size + MARGIN)
 
# Initialize pygame
pygame.init()
 
# Set the WIDTH and HEIGHT of the screen
WINDOW_SIZE = [(HEIGHT + MARGIN) * size + MARGIN  + 250, (WIDTH + MARGIN) * size + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

player_list = [Player("Gabe", 1), Player("Kevin", 2), Player("Alissa", 3), Player("John V", 4)]
empty_players = []
finished_players = []
game_board = Board(size, [1,2,3,4])

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
    n_p = (a_p + 1) % len(player_list)
    next_player = player_list[n_p]
    cnrs = game_board.get_color_corners(next_player.get_color())
    print("Passing to player ", next_player.get_color())
    tp = Piece(next_player.get_color(), 'ONE')
    mvs = game_board.get_moves_list(next_player, cnrs)
    for x in mvs:
        print(x)
    return n_p


# -------- Main Program Loop -----------
while not done:
    if finished_players == player_list:
        done == True

    for event in pygame.event.get():  # User did something
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
                        empty_players.append(active_player)
                        finished_players.append(active_player)
                    active_player = pass_turn(active_player)
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
    
    current_name = player_list[active_player].get_name()
    message_display(current_name, (HEIGHT + MARGIN) * size + MARGIN  + 125, 50, 25)

    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

