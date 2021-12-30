from typing import Dict
import pygame
from pygame.rect import Rect
import engine
import pieces


"""
BLOCK = 100  # size of one space (px)
WINDOW = BLOCK * 8  # size of board (px)
"""
WIDTH = HEIGHT = 512 
DIMENSION = 8  # 8*8
SQ_SIZE = HEIGHT // DIMENSION  
MAX_FPS = 20 # FOR ANIMATIONS
IMAGES = {}



def load_images():
    pieces = ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load(f"images/{piece}.png")


"""
getting a list of all possible sq
"""
def get_all_possible_sq(game_state, start_sq):
    all_possible_sq = []
    row, column = start_sq
    piece = game_state.board[row][column]

    if piece[1] == 'K':
        king = pieces.King()
        all_possible_sq = king.get_all_possible_sq(start_sq=(row, column), board=game_state.board)
        # highlight(screen, gs, (row, column) , all_possible_sq)
        # print(all_possible_sq)

    elif piece[1] == 'Q':
        queen = pieces.Queen()
        all_possible_sq = queen.get_all_possible_sq(start_sq=(row, column), board=game_state.board)

    elif piece[1] == 'B':
        bishop = pieces.Bishop()
        all_possible_sq = bishop.get_all_possible_sq(start_sq=(row, column), board=game_state.board)

    elif piece[1] == 'N':
        knight = pieces.Knight()
        all_possible_sq = knight.get_all_possible_sq(start_sq=(row, column), board=game_state.board)


    elif piece[1] == 'R':
        rook = pieces.Rook()
        all_possible_sq = rook.get_all_possible_sq(start_sq=(row, column), board=game_state.board)

    elif piece[1] == 'P':
        pawn = pieces.Pawn()
        all_possible_sq = pawn.get_all_possible_sq(start_sq=(row, column), board=game_state.board)


    return all_possible_sq




"""
1- draw the blocks on the board
2- draw the pieces on the board
"""
def draw_board(screen, game_state): #selected_sq
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if row%2 == 0 and column%2 == 0 or row%2 == 1 and column%2 == 1:
                color = pygame.Color(240, 217, 181)
            else:
                color = pygame.Color(181, 136, 99)
            
            # draw the board
            pygame.draw.rect(screen, color, pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)) 

            # highlight(screen, game_state, selected_sq=, all_possible_sq=)

            # draw the pieces on the board
            piece = game_state.board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                


"""
Highlighting all the possible moves of the selected piece
"""
def highlight(screen, game_state, selected_sq, all_possible_sq):
    if selected_sq != ():
        row, column = selected_sq
        if game_state.white_turn:
            color = 'w'
        else:
            color = 'b'

        if game_state.board[row][column][0] == color:

            # highlight the selected sq
            surface = pygame.Surface((SQ_SIZE, SQ_SIZE))
            surface.set_alpha(200) #transparancy value -> 0:transparent; 255:opaque;
            
            surface.fill(pygame.Color("blue"))
            screen.blit(surface, (column*SQ_SIZE, row*SQ_SIZE))

            # highlight the all possible moves
            surface.fill(pygame.Color("yellow"))
            for sq in all_possible_sq:
                screen.blit(surface, (sq[1]*SQ_SIZE, sq[0]*SQ_SIZE))

                

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


    print("-------------------------------------- WELCOME --------------------------------------")
    print("1) Press <ctrl+R> for reseting the game")
    print("2) Press <ctrl+Z> for Undo")
    print("3) Press <ctrl+Y> for Redo")
    print("4) Press <ctrl+D> for showing dead pieces")
    print("Move Log:")
    print()

    running = True
    while running:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos() # (x, y)
                column = position[0] // SQ_SIZE
                row = position[1] // SQ_SIZE

                all_possible_sq = get_all_possible_sq(gs, (row, column))
                highlight(screen, gs, (row, column), all_possible_sq)
                pygame.display.flip()


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
                        if queen.is_valid_move(start_sq, end_sq, gs.board):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

                    elif selected_piece[1] == 'B':
                        bishop = pieces.Bishop()
                        if bishop.is_valid_move(start_sq, end_sq, gs.board):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

                    elif selected_piece[1] == 'N':
                        knight = pieces.Knight()
                        if knight.is_valid_move(start_sq, end_sq):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

                    elif selected_piece[1] == 'R':
                        rook = pieces.Rook()
                        if rook.is_valid_move(start_sq, end_sq, gs.board):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

                    elif selected_piece[1] == 'P':
                        pawn = pieces.Pawn()
                        color = selected_piece[0]
                        if pawn.is_valid_move(start_sq, end_sq, color, gs.board):
                            gs.move(start_sq, end_sq, selected_piece, captured_piece)

                    # else:
                    #     gs.move(start_sq, end_sq, selected_piece, captured_piece)


                    # reset user clicks
                    selected_sq = () 
                    clicks = []


            elif e.type == pygame.KEYDOWN:
                # ctrl + z -> undo
                if e.key == pygame.K_z:
                    gs.undo()
                
                # ctrl + y -> redo
                elif e.key == pygame.K_y:
                    gs.redo()

                # ctrl + r -> reset
                elif e.key == pygame.K_r:
                    gs.reset()
                
                elif e.key == pygame.K_d:
                    for piece in gs.dead_pieces:
                        color = "white" if piece[0] == 'w' else "black"
                        dead_piece = gs.piece_names[piece[1]]
                        message = f"{color} {dead_piece}"
                        print(f"Dead Pieces: {message}", end=", ")
                    print()
                    
            
            
        
                    


        # draw_game_state(screen, game_state=gs)
        draw_board(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip() # flip?? redrwas the display


        



if __name__ == "__main__":
    main()

