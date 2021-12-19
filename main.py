import pygame
import engine

"""
BLOCK = 100  # size of one space (px)
WINDOW = BLOCK * 8  # size of board (px)
"""
WIDTH = HEIGHT = 512 # 400
DIMENSION = 8 # 8*8
SQ_SIZE = HEIGHT // DIMENSION # BLOCK = 
MAX_FPS = 15 # FOR ANIMATIONS
IMAGES = {}


def load_images():
    pieces = ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load(f"images/{piece}.png")



"""
1- draw the blocks on the board
2- draw the pieces on the board
"""
def draw_board(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if row%2 == 0 and column%2 == 0 or row%2 == 1 and column%2 == 1:
                color = pygame.Color("white")
            else:
                color = pygame.Color("gray")

            pygame.draw.rect(screen, color, pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)) ## WTF?

            # draw the pieces on the board
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))




# """
# 1- draw the pieces on the board
# """
# def draw_pieces(screen, board):
#     for row in range(DIMENSION):
#         for column in range(DIMENSION):
#             piece = board[row][column]
#             if piece != "--":
#                 screen.blit(IMAGES[piece], pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))



# """
# 1- draw the graphics of the current game state
# """
# def draw_game_state(screen, game_state):
#     draw_board(screen) 
#     draw_pieces(screen, game_state.board)



"""
1- initialize pygame
2- set screen
"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = engine.GameState()
    load_images()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        # draw_game_state(screen, game_state=gs)
        draw_board(screen, gs.board)
        clock.tick(MAX_FPS)
        pygame.display.flip() # flip??
        



if __name__ == "__main__":
    main()

