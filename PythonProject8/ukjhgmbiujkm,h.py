import random
import copy
import math
import time  # For tracking AI thinking time

# --- CONSTANTS ---
W_PIECE = 'w'
B_PIECE = 'b'
W_KING = 'W'
B_KING = 'B'
EMPTY = ' '
AI_PLAYER = B_PIECE  # AI plays black pieces
HUMAN_PLAYER = W_PIECE  # Human plays white pieces
MAX_SEARCH_DEPTH = 5  # How many moves ahead the AI looks (higher is stronger but slower)


class CheckersGame:
    """
    Implements the Checkers game logic, including Minimax AI with Alpha-Beta Pruning.
    """

    def __init__(self, size=8):
        # Initialize game state
        self.size = size
        self.board = self.setup_board()
        self.current_turn = AI_PLAYER  # AI always starts first (Black)
        self.is_multijump = False
        self.last_jump = None  # Tracks the piece location if a multi-jump is forced

    @staticmethod
    def setup_board():
        """Sets up the standard 8x8 checkers board."""
        board = [[EMPTY for _ in range(8)] for _ in range(8)]

        # Place black pieces ('b') on rows 0, 1, 2
        for r in range(3):
            for c in range(8):
                if (r + c) % 2 == 1:
                    board[r][c] = B_PIECE

        # Place white pieces ('w') on rows 5, 6, 7
        for r in range(5, 8):
            for c in range(8):
                if (r + c) % 2 == 1:
                    board[r][c] = W_PIECE
        return board

    def print_board(self):
        """Prints the current state of the board with coordinates."""
        print("-" * (self.size * 2 + 2))
        print("  " + " ".join(map(str, range(self.size))))
        for r in range(self.size):
            print(str(r) + " " + " ".join(self.board[r]))
        print("-" * (self.size * 2 + 2))

    # --- CORE GAME LOGIC HELPERS ---

    def _get_opponent(self, piece_char):
        """Returns the opposite player's base piece char."""
        return W_PIECE if piece_char in [B_PIECE, B_KING] else B_PIECE

    def _is_on_board(self, r, c):
        """Checks if a coordinate is within the board bounds."""
        return 0 <= r < self.size and 0 <= c < self.size

    def _get_piece_valid_directions(self, piece):
        """Returns possible row direction changes for a piece (pawn/king)."""
        if piece == B_PIECE:  # Black moves downwards (rows increase)
            return [1]
        elif piece == W_PIECE:  # White moves upwards (rows decrease)
            return [-1]
        elif piece in [B_KING, W_KING]:  # Kings move both ways
            return [1, -1]
        return []

    def _parse_input(self, prompt):
        """
        Handles robust user input for coordinates, supporting various formats (e.g., '5 0', '5,0', '50').
        Returns (r, c) as integers, or (None, None) if the input loop should restart.
        """
        while True:
            try:
                raw_input = input(prompt).strip()
                if not raw_input:
                    # Allow user to hit enter to re-read prompt
                    return None, None

                    # Normalize input: replace commas with spaces
                cleaned_input = raw_input.replace(',', ' ').strip()

                # Try splitting by space
                parts = cleaned_input.split()

                if len(parts) == 2:
                    # Format: '5 0'
                    r, c = map(int, parts)
                    return r, c

                # Try combined digits format (e.g., '50')
                if len(parts) == 1 and len(parts[0]) == 2 and parts[0].isdigit():
                    r = int(parts[0][0])
                    c = int(parts[0][1])
                    return r, c

                print(
                    "Invalid input format. Please enter two numbers separated by a space or a comma (e.g., 5 0 or 5,0).")

            except ValueError:
                print("Invalid input format. Please ensure both inputs are numerical digits (e.g., 5 0).")
            except Exception as e:
                print(f"An unexpected input error occurred: {e}")

    def get_valid_moves(self, board, player_char, check_multijump_from=None):
        """
        Generates all legal moves for the current player.
        If a jump is available, ONLY jumps are returned (mandatory jump rule).
        Returns a dictionary: { (from_r, from_c): [ (to_r, to_c, captured_r, captured_c), ... ], ... }
        """
        moves = {}
        jumps = {}

        player_pawns = [player_char, player_char.upper()]

        # Determine which pieces to check
        start_points = []
        if check_multijump_from:
            start_points = [check_multijump_from]
        else:
            for r in range(self.size):
                for c in range(self.size):
                    if board[r][c] in player_pawns:
                        start_points.append((r, c))

        for r, c in start_points:
            piece = board[r][c]
            directions = self._get_piece_valid_directions(piece)

            piece_moves = []

            for row_dir in directions:
                for col_dir in [-1, 1]:
                    # 1. Check for simple move (1 space diagonal)
                    tr, tc = r + row_dir, c + col_dir
                    if not check_multijump_from and self._is_on_board(tr, tc) and board[tr][tc] == EMPTY:
                        piece_moves.append((tr, tc, None, None))  # Move: to_r, to_c, captured_r, captured_c

                    # 2. Check for jump (2 spaces diagonal)
                    jr, jc = r + row_dir, c + col_dir  # Jumped piece location
                    tr2, tc2 = r + 2 * row_dir, c + 2 * col_dir  # Landing spot

                    if self._is_on_board(tr2, tc2) and board[tr2][tc2] == EMPTY:
                        # Check if the jumped piece is an opponent's piece
                        jumped_piece = board[jr][jc]
                        if jumped_piece != EMPTY and jumped_piece not in player_pawns:
                            # Valid jump found
                            if (r, c) not in jumps:
                                jumps[(r, c)] = []
                            jumps[(r, c)].append((tr2, tc2, jr, jc))

            # If no jumps found, add normal moves for this piece
            if not (r, c) in jumps and piece_moves:
                moves[(r, c)] = piece_moves

        if jumps:
            # Mandatory jump rule: If any jump is available, only jumps are legal moves.
            return jumps

        return moves

    def _execute_move(self, board, move):
        """
        Executes a move and returns the new board state. This is a pure function.
        Move format: ((fr, fc), (tr, tc, jr, jc))
        """
        (fr, fc), (tr, tc, jr, jc) = move
        new_board = copy.deepcopy(board)

        piece = new_board[fr][fc]

        # 1. Move the piece
        new_board[tr][tc] = piece
        new_board[fr][fc] = EMPTY

        # 2. Capture the opponent piece if it was a jump
        if jr is not None:
            new_board[jr][jc] = EMPTY

        # 3. Handle Kinging
        if piece == W_PIECE and tr == 0:
            new_board[tr][tc] = W_KING
        elif piece == B_PIECE and tr == self.size - 1:
            new_board[tr][tc] = B_KING

        return new_board

    def check_for_win(self, board):
        """Checks for win/loss/continue state. Returns the winner char or None."""
        w_count = sum(row.count(W_PIECE) + row.count(W_KING) for row in board)
        b_count = sum(row.count(B_PIECE) + row.count(B_KING) for row in board)

        if w_count == 0:
            return B_PIECE  # Black wins
        if b_count == 0:
            return W_PIECE  # White wins

        # Check if the current player has no moves (stalemate/loss)
        if not self.get_valid_moves(board, self.current_turn):
            return self._get_opponent(self.current_turn)

        return None  # Game continues

    # --- AI (MINIMAX) LOGIC ---

    def evaluate_board(self, board, player_char):
        """
        Evaluation function: Scores based on material advantage, king status, and board positioning.
        """
        score = 0

        piece_val = 10
        king_val = 35

        player_pawns = [player_char, player_char.upper()]

        for r in range(self.size):
            for c in range(self.size):
                piece = board[r][c]

                if piece == player_pawns[0]:  # Regular piece
                    score += piece_val
                    # Reward proximity to the king row (r=0 for W, r=7 for B)
                    if player_char == B_PIECE:
                        score += (r / self.size) * 5
                    else:
                        score += ((self.size - 1 - r) / self.size) * 5

                elif piece == player_pawns[1]:  # King
                    score += king_val

                elif piece != EMPTY:  # Opponent piece

                    # Determine opponent's base piece type
                    opponent_piece_type = self._get_opponent(player_char)

                    if piece == opponent_piece_type:  # Opponent Regular piece
                        score -= piece_val
                        # Penalize opponent proximity to their king row
                        if player_char == B_PIECE:
                            score -= ((self.size - 1 - r) / self.size) * 5
                        else:
                            score -= (r / self.size) * 5

                    elif piece == opponent_piece_type.upper():  # Opponent King
                        score -= king_val

        return score

    def minimax(self, board, depth, alpha, beta, is_maximizing_player, player_char):
        """
        Minimax algorithm with Alpha-Beta Pruning.
        Returns (score, move_path)
        """

        # Base Case 1: Game Over
        winner = self.check_for_win(board)
        if winner == player_char:
            return (10000000000 + depth, None)  # Win
        if winner == self._get_opponent(player_char):
            return (-10000000000 - depth, None)  # Loss

        # Base Case 2: Max Depth Reached
        if depth == 0:
            return (self.evaluate_board(board, player_char), None)

        # Determine which player's turn it is in the search tree
        current_player = player_char if is_maximizing_player else self._get_opponent(player_char)
        all_possible_moves = self.get_valid_moves(board, current_player)

        # Minimax Search
        if is_maximizing_player:
            max_eval = -math.inf
            best_move = None

            for start_pos, end_moves in all_possible_moves.items():
                for end_move in end_moves:
                    move = (start_pos, end_move)
                    new_board = self._execute_move(board, move)

                    # Recurse: next turn is minimizing
                    evaluation, _ = self.minimax(
                        new_board, depth - 1, alpha, beta, False, player_char
                    )

                    if evaluation > max_eval:
                        max_eval = evaluation
                        best_move = move

                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break  # Alpha-Beta Pruning
                if beta <= alpha:
                    break
            return (max_eval, best_move)

        else:  # Minimizing player
            min_eval = math.inf
            best_move = None

            for start_pos, end_moves in all_possible_moves.items():
                for end_move in end_moves:
                    move = (start_pos, end_move)
                    new_board = self._execute_move(board, move)

                    # Recurse: next turn is maximizing
                    evaluation, _ = self.minimax(
                        new_board, depth - 1, alpha, beta, True, player_char
                    )

                    if evaluation < min_eval:
                        min_eval = evaluation
                        best_move = move

                    beta = min(beta, min_eval)
                    if beta <= alpha:
                        break  # Alpha-Beta Pruning
                if beta <= alpha:
                    break
            return (min_eval, best_move)

    def find_best_move(self, board, player_char, depth):
        """Wrapper to call Minimax and return the best move."""
        print(f"\nAI ({player_char.upper()}) is thinking... (Depth {depth})")
        start_time = time.time()

        score, best_move = self.minimax(
            board,
            depth,
            -math.inf,
            math.inf,
            True,
            player_char
        )

        end_time = time.time()
        print(f"AI chose move with score: {score}. Time taken: {end_time - start_time:.2f} seconds.")
        return best_move

    # --- GAME LOOP EXECUTION ---

    def _execute_turn_move(self, move):
        """
        Executes a move for the current turn, updates state, and checks for multi-jump.
        Returns True if the current player must jump again, False otherwise.
        """
        self.board = self._execute_move(self.board, move)

        # Check for multi-jump opportunity
        (fr, fc), (tr, tc, jr, jc) = move

        # If the move was a jump (jr is not None)
        if jr is not None:
            # Check if the game ended after the capture
            if self.check_for_win(self.board) is not None:
                return False

                # Check for further jumps from the new position (tr, tc)
            # We use the board state *after* the move and capture
            possible_jumps = self.get_valid_moves(self.board, self.current_turn, check_multijump_from=(tr, tc))

            # If the only moves found are jumps from the new piece location
            if possible_jumps:
                # Forced multi-jump: stay on the same turn
                self.is_multijump = True
                self.last_jump = (tr, tc)
                return True  # Continue turn
            else:
                self.is_multijump = False
                self.last_jump = None
                return False  # End turn
        else:
            self.is_multijump = False
            self.last_jump = None
            return False  # End turn

    def play(self):
        """Main game loop for human vs AI play."""
        print("Welcome to Conner's checkers! Here are the instructions:")
        print(
            f"You are the White pieces ({HUMAN_PLAYER.upper()}), and the AI is the Black pieces ({AI_PLAYER.upper()}).")
        print("The goal is to capture all of your opponent's pieces.")
        print(f"AI ({AI_PLAYER.upper()}) will go first.")

        while True:
            self.print_board()
            winner = self.check_for_win(self.board)
            if winner:
                print(f"\n--- {winner.upper()}'s wins! Game over! ---")
                break

            player_name = "AI" if self.current_turn == AI_PLAYER else "Human"
            print(f"\n--- {player_name} ({self.current_turn.upper()})'s turn ---")

            if self.current_turn == AI_PLAYER:
                # --- AI TURN ---
                move = self.find_best_move(self.board, AI_PLAYER, MAX_SEARCH_DEPTH)

                if move is None:
                    print(f"AI has no legal moves. {HUMAN_PLAYER.upper()} wins!")
                    break

                ((fr, fc), (tr, tc, jr, jc)) = move
                print(f"AI chose: ({fr}, {fc}) to ({tr}, {tc})")

                # Execute the move and check for multi-jump
                continue_turn = self._execute_turn_move(move)

                # Simplified: AI makes the single best move/jump and the turn switches.
                # A full AI would recursively search the best multi-jump sequence.
                if not continue_turn:
                    self.current_turn = HUMAN_PLAYER


            else:  # --- HUMAN TURN ---

                valid_moves = self.get_valid_moves(self.board, HUMAN_PLAYER, self.last_jump)

                # Inform the player about mandatory moves
                must_jump = any(jc is not None for moves in valid_moves.values() for _, _, jr, jc in moves)

                if self.last_jump and self.is_multijump:
                    print(
                        f"**FORCED MULTI-JUMP** You must continue the jump with the piece at {self.last_jump[0]}, {self.last_jump[1]}.")
                elif must_jump:
                    print("**MANDATORY JUMP** A jump is available and MUST be taken!")

                is_valid = False
                while not is_valid:
                    # STEP 1: Get the piece to move
                    fr, fc = self._parse_input(
                        "Enter the ROW and COLUMN of the piece you want to move (e.g., 5 0, 5,0, or 50): ")

                    if fr is None:
                        continue  # Re-prompt if input was empty or poorly formatted

                    start_pos = (fr, fc)

                    # --- Enhanced Error Checking for Piece Selection ---
                    if not self._is_on_board(fr, fc):
                        print("Error: The selected coordinates are off the board.")
                        continue

                    piece = self.board[fr][fc]
                    player_pieces = [HUMAN_PLAYER, W_KING]

                    if piece == EMPTY:
                        print("Error: That square is empty. Please select a square with one of your pieces.")
                        continue

                    if piece not in player_pieces:
                        print(
                            f"Error: That piece ({piece}) belongs to the AI. Please select a White piece ({HUMAN_PLAYER.upper()} or {W_KING}).")
                        continue
                    # --- End Enhanced Error Checking ---

                    # Check if the start position is a legal move source
                    if start_pos not in valid_moves:
                        if self.is_multijump:
                            print(
                                f"Invalid piece selected. You must continue the jump from {self.last_jump[0]}, {self.last_jump[1]}.")
                        elif must_jump:
                            print(
                                "Invalid piece selection. You must select a piece that can perform the mandatory jump.")
                        else:
                            print("The selected piece has no legal moves (perhaps it is blocked).")
                        continue

                    # Show available destinations
                    destinations = valid_moves[start_pos]

                    # Check if the piece is only capable of jumps
                    is_jump_only = all(jr is not None for _, _, jr, jc in destinations)

                    if is_jump_only:
                        print(
                            f"Available JUMP destinations for ({fr}, {fc}): {[(tr, tc) for tr, tc, _, _ in destinations]}")
                    else:
                        print(f"Available destinations for ({fr}, {fc}): {[(tr, tc) for tr, tc, _, _ in destinations]}")

                    # STEP 2: Get the destination
                    tr, tc = self._parse_input(f"Enter the ROW and COLUMN destination for ({fr}, {fc}): ")

                    if tr is None:
                        continue  # Re-prompt if input was empty or poorly formatted

                    # Check if the destination is a legal move
                    move = None
                    for move_option in destinations:
                        target_r, target_c, jr, jc = move_option
                        if target_r == tr and target_c == tc:
                            move = (start_pos, move_option)
                            break

                    if move:
                        # Execute the move
                        continue_turn = self._execute_turn_move(move)

                        if continue_turn:
                            # Multi-jump is forced, loop continues for the same player
                            print(f"Jump successful. Piece moved to ({tr}, {tc}). You must jump again.")
                        else:
                            # Turn ends, switch player
                            self.current_turn = AI_PLAYER
                        is_valid = True

                    else:
                        print("Invalid destination: The coordinate is not a legal move for the selected piece.")


# --- RUN GAME ---
if __name__ == '__main__':
    # Initialize game
    game = CheckersGame()

    # Start the game loop
    game.play()