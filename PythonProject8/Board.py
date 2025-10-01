class Board:
    def __init__(self):
        self.size = 8
        self.board = [0, 2, 0, 2, 0, 2, 0, 2]
        self.setup_board()

def setup_board(self):
    for i in range(3):
        for j in range(self.size):
            if(i + j) % 2 == 1:
                self.board[i][j] = 'b'
        for i in range(6, 8):
            for j in range(self.size):
                if(i + j) % 2 == 1:
                    self.board[i][j] = 'w'

def display(self):







