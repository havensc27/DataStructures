class Board:
    def __init__(self):
        self.size = 8
        self.board = [0, 2, 0, 2, 0, 2, 0, 2]
        self.setup_board()

def setup_board(self):
    for row in range(3):
        for col in range(self.size):
            if(row + col) % 2 == 1:
                self.board[row][col] = 'b'
        for row in range(6, 8):
            for col in range(self.size):
                 if(row + col) % 2 == 1:
                    self.board[row][col] = 'w'

def display(self):
    print(" ", end="")
    for row in range(self.size):
        print(row, end="")
    print()
    for row in range(self.size):
        print(row, end="")
    print(" ".join(self.board[row]))

def move_piece(self, from_row, from_col, to_row, to_col, player):
    if self.board[from_row][from_col].lower() != player:
        print("Invalid move: You must move your own piece")
        return False
    if self.board[to_row][to_col] != '':
        print("Invalid move: destination not empty")
        return False
    if (to_row - from_col) == 1 and (to_row - from_col) == 1:
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[to_row][to_col] = ' '
    return True
    elif (to_row - from_col) == 2 and (to_row - from_col) == 2:
        mid_row = (from_row + to_col)/2
        mid_col = (from_col + to_col)/2
    if self.board[to_row][to_col].lower() != player and self.board[mid_row][mid_col] != player:
        self.board[from_row][from_col] = ''
        self.board[mid_row][mid_col] = ''
        return True
    else:
        print("Invalid jump: No opposite checker to capture.")
    else:
        print("Invalid move: Move Diagonally.")
    return False

def has_pieces(self, player):






