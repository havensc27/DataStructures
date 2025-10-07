print("Welcome to Conner's checkers! Here are the instructions: You will either be the red or black piece (randomized), and whoever claims all the opposing pieces wins!")

class Board:
    def __init__(self):
        self.size = 8
        self.board = [
            [0, 2, 0, 2, 0, 2, 0, 2]
            [2, 0, 2, 0, 2, 0, 2, 0]
            [0, 2, 0, 2, 0, 2, 0, 2]
            [2, 0, 2, 0, 2, 0, 2, 0]
            [0, 2, 0, 2, 0, 2, 0, 2]
            [2, 0, 2, 0, 2, 0, 2, 0]
            [0, 2, 0, 2, 0, 2, 0, 2]
            [2, 0, 2, 0, 2, 0, 2, 0]]
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

    row_diff = to_row - from_row
    col_diff = to_col - from_col

    if (to_row - from_col) == 1 and (to_row - from_col) == 1:
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[to_row][to_col] = ' '
        return True

    elif (row_diff) == 2 and (col_diff) == 2:
        mid_row = (from_row + to_row)//2
        mid_col = (from_col + to_col)//2
        mid_piece = self.board[mid_row][mid_col]

        if mid_piece.lower() != player and mid_piece != '':
            self.board[to_row][to_col] = self.board[from_row][from_col]
            self.board[from_row][from_col] = ''
            self.board[mid_row][mid_col] = ''
            return True
        else:
            print("Invalid jump: No opposite checker to capture.")
            return False
    else:
        print("Invalid move: Move Diagonally.")
        return False

def has_pieces(self, player):
    return any(cell.lower() == player for row in self.board for cell in row)

def play_checkers():
    board = Board()
    players = ['player1', 'player2']
    turn = 0

    print("Welcome to checkers!")
    print("Enter moves as: from_row, from_col, to_row, to_col")

    while True:
        board.display()
        current_player = players[turn % 2]
        print("Current Players turn: (current_player.upper())'s turn.")

        try:
            move = input("Enter your move: ").strip().split()
            if len(move) != 4:
                print("Invalid input. Enter four numbers.")
                continue
            fr, fc, tr, tc = map(int, move)
            if not all(0 <= x < 8 for x in [fr, fc, tr, tc]):
                print("Invalid input. Numbers must be between 0 and 7.")
                continue
        except ValueError:
            print("Invalid format. Use numbers only.")
            continue

        if board.move_piece(fr, fc, tr, tc, current_player):
            opponent = players[(turn + 1) % 2]
            board.display()
            print("{f} (current_player.upper())'s")
            break
        turn += 1

    if __name__ == "__main__":
        play_checkers()













