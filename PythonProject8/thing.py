def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

board = []
for i in range(8):
    board.append([0] * 8)

for g in range(8):
    if g < 3 or i >= 4:
        board[i][g] = 1

print_board(board)

class Board:
    def __init__(self):
        self.size = 8
        self.board = [
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0]]
        self.setup_board()

    def display(self):
        print(" ", end="")
        for row in range(self.size):
            print(row, end="")
        for row in range(self.size):
            print(row, end="")
        print(" ".join(str(cell) for cell in self.board[row]))