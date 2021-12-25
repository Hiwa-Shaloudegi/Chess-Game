"""
1- Valid moves
2- Storing all moves
"""

class GameState: # class Game:
    def __init__(self):
        self.board = [

            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
            
        ]

        self.white_turn = True
        self.all_moves = []
        self.dead_pieces = []
        self.undo_moves = []


    def move(self, start_sq, end_sq, piece1, piece2):

        start_row = start_sq[0]
        start_column = start_sq[1]
        end_row = end_sq[0]
        end_column = end_sq[1]
        
        if (self.white_turn and piece1[0] == 'w') or (not self.white_turn and piece1[0] == 'b'):
            
            if piece1[0] != piece2[0]:
                self.board[start_row][start_column] = "--"
                self.board[end_row][end_column] = piece1

            if piece2 != "--":
                self.dead_pieces.append(piece2)

            move_info = ()
            move_info = piece1[0], piece1, piece2, start_sq, end_sq   # move_info: ('w', 'wP', 'bN', (x1, y1), (x2, y2))
            self.all_moves.append(move_info)

            self.white_turn = not self.white_turn




    def undo(self):
        if len(self.all_moves) != 0:

            last_move = self.all_moves.pop()
            self.undo_moves.append(last_move)

            start_row = last_move[3][0]
            start_column = last_move[3][1]
            end_row = last_move[4][0]
            end_column = last_move[4][1]

            self.board[start_row][start_column] = last_move[1]
            self.board[end_row][end_column] = last_move[2]

            self.white_turn = not self.white_turn

    

    def redo(self):
        if len(self.undo_moves) != 0:

            last_move = self.undo_moves.pop()
            self.all_moves.append(last_move)

            self.move(last_move[3], last_move[4], last_move[1], last_move[2])

            self.white_turn = not self.white_turn



    def reset(self):
        self.board = [

            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
            
        ]

        self.white_turn = True
        self.all_moves = []
        self.dead_pieces = []
        self.undo_moves = []







