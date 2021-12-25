from typing import Dict
import pygame
from pygame.rect import Rect
import engine
import pieces


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
                color = pygame.Color(240, 217, 181)
            else:
                color = pygame.Color(181, 136, 99)

            pygame.draw.rect(screen, color, pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)) 

            # draw the pieces on the board
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                
                

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


    selected_sq = () # last click of the user (row, column)
    clicks = []      #  [(row1, column1), (row2, column2)]

    running = True
    while running:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos() # (x, y)
                column = position[0] // SQ_SIZE
                row = position[1] // SQ_SIZE

                if  selected_sq != (row, column):
                    selected_sq = (row, column)
                    clicks.append(selected_sq)
                else:
                    selected_sq = ()           # (row, column)
                    clicks = []                # [(row1, column1), (row2, column2)]


                if len(clicks) == 2:

                    start_sq = clicks[0]
                    end_sq = clicks[1]

                    start_row = start_sq[0]
                    start_column = start_sq[1]
                    end_row = end_sq[0]        
                    end_column = end_sq[1]     

                    selected_piece = gs.board[start_row][start_column]
                    captured_piece = gs.board[end_row][end_column]

                    # move function
                    if selected_piece[1] == 'K':
                        king = pieces.King()
                        if king.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)


                    elif selected_piece[1] == 'Q':
                        queen = pieces.Queen()
                        if queen.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)
                            # print(queen.get_all_possible_sq())

                    elif selected_piece[1] == 'B':
                        bishop = pieces.Bishop()

                        all_possible_sq = bishop.get_all_possible_sq(start_sq, gs.board)
                        print(all_possible_sq)

                        if bishop.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)


                    elif selected_piece[1] == 'N':
                        knight = pieces.Knight()


                        all_possible_sq = knight.get_all_possible_sq(start_sq, gs.board)
                        print(all_possible_sq)
                        # for sq in all_possible_sq:
                        #     pygame.draw.rect(screen, "red", Rect(sq[1]*SQ_SIZE, sq[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

                        if knight.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)


                    elif selected_piece[1] == 'R':
                        rook = pieces.Rook()
                        if rook.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

            
                    elif selected_piece[1] == 'P':
                        pawn = pieces.Pawn()
                        color = selected_piece[0]
                        if pawn.is_valid_move(start_sq, end_sq, color):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)


                    # else:
                    #     gs.move(start_sq, end_sq, selected_piece, captured_piece)




                    # reset user clicks
                    selected_sq = () 
                    clicks = []


            elif e.type == pygame.KEYDOWN:
                # ctrl + z
                if e.key == pygame.K_z:
                    gs.undo()
                
                # ctrl + y
                elif e.key == pygame.K_y:
                    gs.redo()

                # ctrl + r
                elif e.key == pygame.K_r:
                    gs.reset()
            
            
        
                    

                    

        # draw_game_state(screen, game_state=gs)
        draw_board(screen, gs.board)
        clock.tick(MAX_FPS)
        pygame.display.flip() # flip?? redrwas the display


        



if __name__ == "__main__":
    main()

