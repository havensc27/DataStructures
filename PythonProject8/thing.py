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

