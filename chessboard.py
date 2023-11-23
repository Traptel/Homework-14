import random


class Chessboard:
    def __init__(self):
        self.board = [
            ['░', '▓', '░', '▓', '░', '▓', '░', '▓'],
            ['▓', '░', '▓', '░', '▓', '░', '▓', '░'],
            ['░', '▓', '░', '▓', '░', '▓', '░', '▓'],
            ['▓', '░', '▓', '░', '▓', '░', '▓', '░'],
            ['░', '▓', '░', '▓', '░', '▓', '░', '▓'],
            ['▓', '░', '▓', '░', '▓', '░', '▓', '░'],
            ['░', '▓', '░', '▓', '░', '▓', '░', '▓'],
            ['▓', '░', '▓', '░', '▓', '░', '▓', '░']
        ]
        self.kings = ['♕', '♛']
        self.pieces = ['♖', '♗', '♘', '♙', '♚', '♜', '♝', '♞', '♟']
        self.placed_pieces = []

    def random_placement(self):
        num_pieces = random.randint(1, len(self.pieces))
        selected_pieces = random.choices(self.pieces, k=num_pieces)
        self.placed_pieces = selected_pieces + self.kings

        while self.placed_pieces:
            row = random.randint(0, len(self.board) - 1)
            col = random.randint(0, len(self.board[0]) - 1)

            if self.board[row][col] in ['█', '░']:
                self.board[row][col] = self.placed_pieces.pop()

    def print_board(self):
        print("   a b c d e f g h")
        print(" ┏━━━━━━━━━━━━━━━━┓ ")
        for i, row in enumerate(self.board):
            row_str = ' '.join(row)
            print(f"{8 - i}│ {row_str.ljust(16)}│")
        print(" ┗━━━━━━━━━━━━━━━━┛")


if __name__ == "__main__":
    chess = Chessboard()

    for _ in range(3):
        chess.random_placement()
        chess.print_board()
