import random

print("Welcome to Conner's checkers! Here are the instructions: ")
print("You will either be the white or black piece (randomized), and whoever claims all the opposing pieces wins!")
print("You have to enter a move with the coordinates (r, c) of your piece, and then the coordinates of where you want to move (r, c)")

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
        print(" " + "--" * (self.size + 1))
        for i in range(self.size):
            print(str(i) + " " + " ".join(self.board[i]))

    def move_piece(self, fr, fc, tr, tc, player):
        piece = self.board[fr][fc]
        opponent = 'b' if player == 'w' else 'w'

        if piece != player: return False
        if self.board[tr][tc] != ' ':
            print("Invalid: Destination is not empty")
            return False

        row_diff = tr - fr
        col_diff = abs(tc - fc)

        if abs(row_diff) == 1 and col_diff == 1:
            if (player == 'w' and row_diff > 0) or (player == 'b' and row_diff < 0):
                print("Invalid move: Pieces must move forward.")
                return False
            self.board[tr][tc] = piece
            self.board[fr][fc] = ' '
            return True

        elif abs(row_diff) == 2 and col_diff == 2:
            if (player == 'w' and row_diff > 0) or (player == 'b' and row_diff < 0):
                print("Invalid move: Pieces must move forward.")
                return False

            mid_row = (fr + tr)//2
            mid_col = (fc + tc)//2
            mid_piece = self.board[mid_row][mid_col]

            if mid_piece == opponent:
                self.board[tr][tc] = piece
                self.board[fr][fc] = ' '
                self.board[mid_row][mid_col] = ' '

                print("\n You took a piece \n")

                return True
            else:
                print("Invalid jump: No enemy checker to capture.")
                return False
        else:
            print("Invalid move: Your move has to be 1 or 2 spots diagonally.")
            return False

    def get_coords(self, prompt, size):
        while True:
           try:
               coords = input(prompt).strip().split()
               if len(coords) != 2:
                   print("Invalid input. Enter 2 numbers (I.E. 4 2).")
                   continue
               r, c = map(int, coords)
               if not (0 <= r < size and 0 <= c < size):
                   print("Invalid Input: Numbers have to be between 0 and 7.")
                   continue
               return r, c
           except ValueError:
               print("Invalid format: Use numbers only.")

    def has_pieces(self, player):
        return any(cell == player for row in self.board for cell in row)

    def play(self):
        players = ['w', 'b']
        random.shuffle(players)
        turn = 0

        while True:
            self.print_board()
            current_player = players[turn % 2]
            player_name = "White" if current_player == 'w' else "Black"
            print(f"\n{player_name} ({current_player})'s turn")

            fr, fc, tr, tc = -1, -1, -1, -1

            while True:
                fr, fc = self.get_coords(f"1. Enter coordinates of your piece. (r, c)", self.size)
                if self.board[fr][fc] != current_player:
                    print(f"Error: You have to select one of your own pieces ({current_player}).")
                else:
                    break

            tr, tc = self.get_coords(f"2. Enter destination of your piece. (r, c)", self.size)

            if self.move_piece(fr, fc, tr, tc, current_player):
                opponent = players[(turn + 1) % 2]
                if not self.has_pieces(opponent):
                    self.print_board()
                    print(f"\n{current_player} wins! Game is over!")
                    break
                turn += 1
            else:
                print("Move failed. Try again.")

game = Checkers()
game.play()