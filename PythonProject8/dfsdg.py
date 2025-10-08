import random

print("Welcome to Conner's checkers! Here are the instructions: ")
print("You will either be the red or black piece (randomized), and whoever claims all the opposing pieces wins!")

class Checkers:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.setup_board()

    def setup_board(self):
        for i in range(self.size):
            for j in range(self.size):
                    if (i + j) % 2 == 1:
                        if i < 3:
                            self.board[i][j] = 'b'
                        elif i > 4:
                            self.board[i][j] = 'w'

    def print_board(self):
        print(" " + " ".join(map(str, range(self.size))))
        for i in range(self.size):
            print(str(i) + " " + " ".join(self.board[i]))

    def move_piece(self, fr, fc, tr, tc, player):
        if self.board[fr][fc].lower() != player:
            print("Invalid move: You must move your own piece")
            return False
        if self.board[tr][tc] != ' ':
            print("Invalid move: destination not empty")
            return False

        row_diff = tr - fr
        col_diff = tc - fc

        if abs(row_diff) == 1 and abs(col_diff) == 1:
            self.board[tr][tc] = self.board[fr][fc]
            self.board[fr][fc] = ' '
            return True

        elif (row_diff) == 2 and (col_diff) == 2:
            mid_row = (fr + tr)//2
            mid_col = (fc + tc)//2
            mid_piece = self.board[mid_row][mid_col]

            if mid_piece.lower() != player and mid_piece != '':
                self.board[tr][tc] = self.board[fr][fc]
                self.board[fr][fc] = ''
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

    def play(self):
        players = ['white', 'black']
        random.shuffle(players)
        turn = 0

        print(f"white = 'w', black = 'b'")
        print(f"{players[0].upper()}'s turn")

        while True:
            self.print_board()
            current_player = players[turn % 2]
            print(f"{current_player.upper()}'s turn.")

            try:
                move = input("Enter your move: fr, fc, tr, tc").strip().split()
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

            if self.move_piece(fr, fc, tr, tc, current_player):
                if not self.has_pieces(players[(turn + 1) % 2]):
                    self.print_board()
                    print(f"\n{current_player.upper()}'s wins! Game over!")
                    break
                turn += 1
