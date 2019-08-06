BLACK = 1
WHITE = -1
EMPTY = 0

FLIP = -1

from typing import List, Tuple

class Board:
    """
    Playing board for Reversi game.
    """
    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [[EMPTY]*dimension for _ in range(dimension)]
        self.turn = "p1"

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

    def is_valid_move(self, x_orig, y_orig, colour) -> List[Tuple[int, int]]:
        """
        Returns list of tiles flip_these to flip if move at x_orig, y_orig
        If return list is empty, invalid move.
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]

        if colour == "black":
            self_tile = BLACK
            other_tile = WHITE
        elif colour == "white":
            self_tile = WHITE
            other_tile = BLACK

        # not empty or not on board
        if x_orig >= self.dimension or y_orig >= self.dimension \
                or self.board[x_orig][y_orig] != 0:
            return []

        flip_these = []

        for xdir, ydir in directions:
            x = x_orig + xdir
            y = y_orig + ydir
            if self.is_on_board(x, y) and self.board[x][y] == other_tile:
                x += xdir
                y += ydir

            if not self.is_on_board(x, y):
                continue

            while self.board[x][y] == other_tile:
                x += xdir
                y += ydir
                if not self.is_on_board(x, y):
                    break

            if not self.is_on_board(x, y):
                continue

            # save tiles to flip:
            if self.board[x][y] == self_tile:
                while True:
                    x -= xdir
                    y -= ydir
                    if x == x_orig and y == y_orig:
                        break
                    flip_these.append((x, y))

        return flip_these

    def is_on_board(self, x, y):
        return 0 <= x < self.dimension and 0 <= y < self.dimension

    def valid_move_exists(self, colour):
        for x in range(self.dimension):
            for y in range(self.dimension):
                if len(self.is_valid_move(x, y, colour)) > 0:
                    return True
        return False

    def get_move(self, player):
        x, y, colour = player.choose_move()
        while len(self.is_valid_move(x, y, colour)) < 1:
            print("Invalid move, try again!")
            x, y, colour = player.choose_move()

        flip_these = self.is_valid_move(x, y, colour)
        self.select_placement(x, y, colour)
        for x, y in flip_these:
            self.board[x][y] *= FLIP

    def next_turn(self):
        if self.turn == "p1":
            self.turn = "p2"
        else:
            self.turn = "p1"

    def final_score(self):
        return sum(sum(self.board[i]) for i in range(self.dimension))

    # def play_again(self):
    #     print("Press 'y' to play again")
    #     return input().lower() == 'y'












