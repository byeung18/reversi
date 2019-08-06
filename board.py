BLACK = 1
WHITE = -1
EMPTY = 0


class Board:
    """
    Playing board for Reversi game.
    """
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [[EMPTY]*dimension for _ in range(dimension)]

        mid = self.dimension // 2
        self.board[mid][mid] = BLACK
        self.board[mid-1][mid-1] = BLACK

        self.board[mid-1][mid] = WHITE
        self.board[mid][mid - 1] = WHITE

    def select_placement(self, x, y, colour):
        if colour == 'black':
            self.board[x][y] = BLACK
        else:
            self.board[x][y] = WHITE

    def display_board(self):
        for i in range(self.dimension):
            print(*self.board[i])

    def is_valid_move(self, x, y):
        ...




