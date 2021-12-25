"""
Pieces classes for creating  objects
"""

class Piece:
    def __init__(self):
        # self.posible_sqs = []
        pass
        

    # def get_all_possible_sq(self, start_sq, board):
    #     for row in range(8):
    #         for column in range(8):
    #             piece = board[row][column]
    #             if self.is_valid_move(start_sq, (row, column)) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
    #                 self.all_possible_sq.append( (row, column) )

    #     return self.all_possible_sq


    # def get_all_possible_sq(self, board, start_sq):
    #     for row in board:
    #         for column in board[row]:
    #             if self.is_valid_move( start_sq, (row, column) ):
    #                 self.posible_sqs.append( (row, column) )
        
    #     return self.posible_sqs




class King(Piece):
    def __init__(self):
        # self.type = 'K'
        super().__init__()
    
    def is_valid_move(self, start_sq, end_sq):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]

        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if  x_dif <= 1 and y_dif <= 1:
            return True
        return False


    # def get_all_possible_sq(self, board, start_sq):
    #     for row in board:
    #         for column in board[row]:
    #             if self.is_valid_move( start_sq, (row, column) ):
    #                 self.posible_sqs.append( (row, column) )
        
    #     return self.posible_sqs






class Queen:
    def __init__(self):
        #self.type = 'Q'
        self.posible_sqs = []

        # super().__init__()



    def is_valid_move(self, start_sq, end_sq):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]

        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if x_dif == y_dif or x_dif == 0 or y_dif == 0:
            return True
        return False


    # def get_all_possible_sq(self, board, start_sq):
    #     for row in board:
    #         for column in board[row]:
    #             if self.is_valid_move( start_sq, (row, column) ):
    #                 self.posible_sqs.append( (row, column) )
        
    #     return self.posible_sqs


class Bishop(Piece):
    def __init__(self):
        # self.type = 'B'
        # super().__init__()
        self.all_possible_sq = []

    def is_valid_move(self, start_sq, end_sq):
    
        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]


        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if x_dif == y_dif:
            return True
        return False


        
    # def get_all_possible_sq(self, start_sq, board):
    #     for row in range(8):
    #         for column in range(8):
    #             piece = board[row][column]
    #             if self.is_valid_move(start_sq, (row, column)) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
    #                 self.all_possible_sq.append( (row, column) )

    #     return self.all_possible_sq


        



class Knight(Piece):
    def __init__(self):
        # self.type = 'N'  
        # super().__init__()
        self.all_possible_sq = []
        pass

    def is_valid_move(self, start_sq, end_sq):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]

        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if (x_dif == 2 and y_dif == 1) or (x_dif == 1 and y_dif == 2):
            return True
        return False

        
    def get_all_possible_sq(self, start_sq, board):
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column)) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )

        return self.all_possible_sq





class Rook:
    def __init__(self):
        # self.type = 'R'
        # super().__init__()
        pass

    def is_valid_move(self, start_sq, end_sq):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]


        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)


        if x_dif == 0 or y_dif == 0:
            return True
        return False




class Pawn:
    def __init__(self):
        # self.has_moved = False
        pass

    def is_valid_move(self,  start_sq, end_sq, color):
        
        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]


        x_dif = self.end_column - self.start_column
        y_dif = self.end_row - self.start_row


        if color == 'w':
            if self.start_row == 1 or self.start_row ==6:
                if  (x_dif == 0 and y_dif == -1) or (x_dif == 0 and y_dif == -2):
                    return True

            elif (x_dif == 0 and y_dif == -1):
                return True

            else:
                return False


        elif color == 'b':
            if self.start_row == 1 or self.start_row ==6:
                if  (x_dif == 0 and y_dif == 1) or (x_dif == 0 and y_dif == 2):
                    return True

            elif (x_dif == 0 and y_dif == 1):
                return True

            else:
                return False