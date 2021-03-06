"""
1- Valid moves
2- Storing all moves
"""
class GameState:
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

        self.piece_names = {
            'P':'pawn',
            'R':'rook',
            'N':'knight',
            'B':'bishop',
            'Q':'queen',
            'K':'king'
        }
        
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.square_names = dict()
        for i in range(8):
            for j in range(8):
                self.square_names[(i, j)] = f"{letters[j]}{8 - i}"


        self.black_king_location = (0, 4)   #### new
        self.white_king_location = (7, 4)   #### new

        self.white_turn = True
        self.check_mate = False     #### new
        self.dead_pieces = []
        self.all_moves = []
        self.undo_moves = []





    def move(self, start_sq, end_sq, piece1, piece2):
        print("-----MOVE-----")


        start_row = start_sq[0]
        start_column = start_sq[1]
        end_row = end_sq[0]
        end_column = end_sq[1]
        
        move_info = ()  # move_info: ('w', 'wP', 'bN', (x1, y1), (x2, y2))
        

        if (self.white_turn and piece1[0] == 'w') or (not self.white_turn and piece1[0] == 'b'):
            
            if piece1[0] != piece2[0]:

                # ----------- Updating kings location -----------
                if piece1 == 'bK':
                    self.black_king_location = (end_sq[0], end_sq[1])
                    move_info = piece1[0], piece1, piece2, start_sq, end_sq   
                    color = "white" if move_info[0] == 'w' else "black"
                    message = ""

                elif piece2 == 'wK':
                    self.white_king_location = (end_sq[0], end_sq[1])
                    move_info = piece1[0], piece1, piece2, start_sq, end_sq   
                    color = "white" if move_info[0] == 'w' else "black"
                    message = ""
                # ----------- End -----------
                
                elif piece1 == 'wP' and end_sq[0] == 0:   # white pawn promotion move 
                    self.board[0][end_sq[1]] = "wQ"
                    self.board[start_sq[0]][start_sq[1]] = "--"

                    move_info = piece1[0], piece1, piece2, start_sq, end_sq
                    color = 'white'
                    message = f"White Pawn Promotion:"

                    
                elif piece1 == 'bP' and end_sq[0] == 7: # balck pawn promotion move
                    self.board[7][end_sq[1]] = "bQ"
                    self.board[start_sq[0]][start_sq[1]] = "--"

                    move_info = piece1[0], piece1, piece2, start_sq, end_sq
                    color = 'black'
                    message = f"Black Pawn Promotion:" 

            
                else:                                   # regular move
                    self.board[start_row][start_column] = "--"
                    self.board[end_row][end_column] = piece1

                    move_info = piece1[0], piece1, piece2, start_sq, end_sq   
                    color = "white" if move_info[0] == 'w' else "black"
                    message = ""



                if piece2 != "--":
                    self.dead_pieces.append(piece2)
                    captured_color= "white" if move_info[2][0] == 'w' else "black"
                    message = message + f"({color} {self.piece_names[move_info[1][1]]} killed {captured_color} {self.piece_names[move_info[2][1]]} <{self.square_names[move_info[3]]} to {self.square_names[move_info[4]]}>)"

                else:
                    message = message + f"({color} {self.piece_names[move_info[1][1]]} moved from <{self.square_names[move_info[3]]} to {self.square_names[move_info[4]]}>)"




                self.all_moves.append(move_info)
                self.undo_moves = []      # self.undo_moves.clear()

                self.white_turn = not self.white_turn
                print(message)




    def is_check(self, all_possible_sq):
        self.white_turn = not self.white_turn

        if self.white_turn:
            if self.black_king_location in all_possible_sq:
                    self.white_turn = not self.white_turn 
                    return True
            else:
                self.white_turn = not self.white_turn 
                return False
        
        elif not self.white_turn:
            if self.white_king_location in all_possible_sq:
                self.white_turn = not self.white_turn 
                return True
            else:
                self.white_turn = not self.white_turn 
                return False







    def undo(self):

        print("-----UNDO-----")

        if len(self.all_moves) != 0:
            if len(self.dead_pieces) != 0:
                self.dead_pieces.pop()

            last_move = self.all_moves.pop()            
            self.undo_moves.append(last_move)

            start_row = last_move[3][0]
            start_column = last_move[3][1] 
            end_row = last_move[4][0]
            end_column = last_move[4][1]

            self.board[start_row][start_column] = last_move[1]      # move_info: ('w', 'wP', 'bN', (x1, y1), (x2, y2))
            self.board[end_row][end_column] = last_move[2]

            self.white_turn = not self.white_turn

     

    def redo(self):
        print("-----REDO-----")

        if len(self.undo_moves) != 0:

            last_move = self.undo_moves.pop()
            print(f"in redo method: Last Move: {last_move}")
            self.all_moves.append(last_move)

            print(f"ALl_MOVES: {self.all_moves}")

            temp = self.undo_moves
            self.move(last_move[3], last_move[4], last_move[1], last_move[2])
            # self.white_turn = not self.white_turn                            ##3# hooray
            if len(self.all_moves) != 0:
                self.all_moves.pop()

            self.undo_moves = temp[:]

   
            # self.white_turn = not self.white_turn




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
        self.undo_moves = []
        self.dead_pieces = []







