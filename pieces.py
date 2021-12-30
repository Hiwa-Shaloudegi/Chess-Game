"""
Pieces classes for creating  objects
"""

from pygame import Color

def check_horizontal_vertical(start_sq, end_sq, board):

    start_row = start_sq[0]
    start_column = start_sq[1]
    end_row = end_sq[0]
    end_column = end_sq[1]

    col = start_column
    r = start_row


    if start_row > end_row:
        up = end_sq
        down = start_sq
    else:
        up = start_sq
        down = end_sq

        
    if start_column > end_column:
        right = start_sq
        left = end_sq
    else:
        right = end_sq
        left = start_sq

            
    for row in range(up[0] + 1, down[0]): 
        if board[row][col] != '--':
            return False

    for column in range(left[1] + 1, right[1]):
        if board[r][column] != '--':
            return False

    return True



def check_diametrical(start_sq, end_sq, board):

    start_row = start_sq[0]
    start_column = start_sq[1]
    end_row = end_sq[0]
    end_column = end_sq[1]

    if start_row > end_row and start_column > end_column:
        direction = "up_left"
    elif start_row < end_row and start_column < end_column :
        direction = "down_right"
    
    if start_row > end_row and start_column < end_column:
        direction = "up_right"
    elif start_row < end_row and start_column > end_column:
        direction = "down_left"


    temp = start_sq
    temp_row = start_sq[0]
    temp_column = start_sq[1]

    while temp != end_sq:
        if direction == "up_left":
            temp_row = temp_row - 1
            temp_column = temp_column - 1
            temp = (temp_row, temp_column)

        elif direction == "up_right":
            temp_row = temp_row - 1
            temp_column = temp_column + 1
            temp = (temp_row, temp_column)
        
        elif direction == "down_right":
            temp_row = temp_row + 1
            temp_column = temp_column + 1
            temp = (temp_row, temp_column)

        elif direction == "down_left":
            temp_row = temp_row + 1
            temp_column = temp_column - 1
            temp = (temp_row, temp_column)
        
        else:
            pass

        if temp != end_sq and board[temp_row][temp_column] != '--':
            return False

    
    return True



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
        # super().__init__()
        self.all_possible_sq = []
        
    
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

        
    def get_all_possible_sq(self, start_sq, board):
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column)) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )

        return self.all_possible_sq







class Queen:
    def __init__(self):
        #self.type = 'Q'
        # super().__init__()
        self.all_possible_sq = []


    def is_valid_move(self, start_sq, end_sq, board):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]

        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if x_dif == 0 or y_dif == 0:
            if check_horizontal_vertical(start_sq, end_sq, board):
                return True

        elif x_dif == y_dif:
            if check_diametrical(start_sq, end_sq, board):
                return True
        
        else:
            return False


        
    def get_all_possible_sq(self, start_sq, board):
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column), board) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )   

        return self.all_possible_sq




class Bishop(Piece):
    def __init__(self):
        # self.type = 'B'
        # super().__init__()
        self.all_possible_sq = []

    def is_valid_move(self, start_sq, end_sq, board):
    
        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]


        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)

        if x_dif == y_dif:
            if check_diametrical(start_sq, end_sq, board):
                return True
        return False


    def get_all_possible_sq(self, start_sq, board):
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column), board) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )

        return self.all_possible_sq


        



class Knight(Piece):
    def __init__(self):
        # self.type = 'N'  
        # super().__init__()
        self.all_possible_sq = []
        

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
        sq = ()
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column)) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    sq = (row, column) 
                    self.all_possible_sq.append(sq)

        return self.all_possible_sq





class Rook:
    def __init__(self):
        # self.type = 'R'
        # super().__init__()
        self.all_possible_sq = []
        

    def is_valid_move(self, start_sq, end_sq, board):

        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]
        color = board[self.start_row][self.start_column][0]

        x_dif = abs(self.end_column - self.start_column)
        y_dif = abs(self.end_row - self.start_row)


        if x_dif == 0 or y_dif == 0 :
            if check_horizontal_vertical(start_sq, end_sq, board):
########################################### FUNCTION
            # col = self.start_column
            # r = self.start_row


            # if self.start_row > self.end_row:
            #     up = end_sq
            #     down = start_sq
            # else:
            #     up = start_sq
            #     down = end_sq

            
            # if self.start_column > self.end_column:
            #     right = start_sq
            #     left = end_sq
            # else:
            #     right = end_sq
            #     left = start_sq

            
            # for row in range(up[0] + 1, down[0]): 
            #     # if (color == 'w' and board[row][col][0] == 'b') or (color == 'b' and board[row][col][0] == 'w'):
            #     if board[row][col] != '--':
            #         return False

            # for column in range(left[1] + 1, right[1]):
            #     if board[r][column] != '--':
            #         return False

########################################## END FUNCTION

                return True

        else:
            return False



    def get_all_possible_sq(self, start_sq, board):
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column), board) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )

        return self.all_possible_sq




class Pawn:
    def __init__(self):
        # self.has_moved = False
        self.all_possible_sq = []


    def is_valid_move(self,  start_sq, end_sq, color, board):
        
        self.start_row = start_sq[0]
        self.start_column = start_sq[1]
        self.end_row = end_sq[0]
        self.end_column = end_sq[1]


        x_dif = self.end_column - self.start_column
        y_dif = self.end_row - self.start_row


        if color == 'w':
            if self.start_row == 6:  
                if  (x_dif == 0 and y_dif == -1) or (x_dif == 0 and y_dif == -2):
                    return True
            
            elif (x_dif == 0 and y_dif == -1) and board[end_sq[0]][end_sq[1]][0] != 'b': # board[end_sq[0]][end_sq[1]] != "--"
                return True

            elif ((x_dif == 1 and y_dif == -1) or (x_dif == -1 and y_dif == -1)) and board[end_sq[0]][end_sq[1]][0] == 'b':
                return True

            else:
                return False


        elif color == 'b':
            if self.start_row == 1:
                if  (x_dif == 0 and y_dif == 1) or (x_dif == 0 and y_dif == 2):
                    return True

            elif (x_dif == 0 and y_dif == 1) and board[end_sq[0]][end_sq[1]][0] != 'w':
                return True

            elif ((x_dif == -1 and y_dif == 1) or (x_dif == 1 and y_dif == 1)) and board[end_sq[0]][end_sq[1]][0] == 'w':
                return True

            else:
                return False



    def get_all_possible_sq(self, start_sq, board):
        color = board[start_sq[0]][start_sq[1]][0]
        for row in range(8):
            for column in range(8):
                piece = board[row][column]
                if self.is_valid_move(start_sq, (row, column), color, board) and piece[0] != board[start_sq[0]][start_sq[1]][0]:
                    self.all_possible_sq.append( (row, column) )

        return self.all_possible_sq
