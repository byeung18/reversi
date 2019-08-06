class Board:
    """
    Playing board for Reversi game.
    """
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [[0]*dimension for _ in range(dimension)]

    def select_placement(self, x, y, colour):
        if colour == 'black':
            self.board[x][y] = 1
        else:
            self.board[x][y] = -1

    def display_board(self):
        for i in range(x):
            print(self.board[i])


