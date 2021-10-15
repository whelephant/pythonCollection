import numpy as np
import pygame
import sys
import math

# global variable in CAPS
ROW_COUNT = 6
COLUMNS = 7

# colours as global variables for easy readability
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# the size of each square and circle
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)

# create a matrix of 0's for the board of the game
def create_board():
    board = np.zeros((ROW_COUNT, COLUMNS))
    return board


# give the row, column, and piece. Set the value in the index board[row][column] == piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# check if there is an empty index in the column
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


# starting from index 0, return the first index with value 0
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# print the board, but flipped
def print_board(board):
    print(np.flip(board, 0))


# pass in the board and the piece to check
def winning_move(board, piece):
    # check for horizontal winning scenario
    for c in range(COLUMNS - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # check for vertical winning scenario
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMNS):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # check for positive slope diagonal winning scenario
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True
    # check for negative slope diagonal winning scenario
    for c in range(COLUMNS - 3):
        # for r in range(ROW_COUNT starting from index 3)
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


# draw a board using pygame.draw
def draw_board(board):
    # for all index's in matrix, draw a blue rectangle and a black circle
    for c in range(COLUMNS):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    # for all index's in matrix, if the index is equal to 1 or 2, draw a red or yellow circle respectively
    for c in range(COLUMNS):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)

# initialize pygame and configure window
pygame.init()
pygame.display.set_caption("Connect 4")
width = COLUMNS * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

# set font using pygame.font
my_font = pygame.font.SysFont("monospace", 75)

game_over = False
turn = 0

# game loop
while not game_over:

    # pygame listens to events
    for event in pygame.event.get():
        # if the x button is pressed, quit
        if event.type == pygame.QUIT:
            sys.exit()

        # detecting mouse motion
        if event.type == pygame.MOUSEMOTION:
            # draw black rectangle to cover the circles
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            # pos_x, or x co-ordinate, equals index 0 of event.pos
            pos_x = event.pos[0]
            # when the turn equals zero, draw a red circle, else, draw a yellow circle
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

        # detecting mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            # Ask for Player 1 Input
            if turn == 0:

                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = my_font.render("PLAYER 1 WINS!!", True, RED)
                        # print label at co-ordinates
                        screen.blit(label, (40, 10))
                        game_over = True

            # Ask for Player 2 Input
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARE_SIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = my_font.render("PLAYER 2 WINS!!", True, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)
            # add one to turn, then modulo to get back to 1, or 0
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
