class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board, row, col):
        raise NotImplementedError("This method should be defined in derived classes")


class King(Piece):
    def valid_moves(self, board, row, col):
        pass  # Logic for King's move


class Queen(Piece):
    def valid_moves(self, board, row, col):
        pass  # Logic for Queen's move


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initializes an 8x8 chess board with pieces
        board = [[None for _ in range(8)] for _ in range(8)]
        # Add pieces to the board
        return board

    def display(self):
        # Display the current state of the board
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move(self, from_pos, to_pos):
        # Move piece logic
        pass


def main():
    chess_board = ChessBoard()
    chess_board.display()

    # Simple turn-based mechanism
    player_turn = "Player 1"

    while True:
        print(f"{player_turn}'s turn")
        # Input handling for move
        # Move logic
        # Switch Player

if __name__ == "__main__":
    main()
