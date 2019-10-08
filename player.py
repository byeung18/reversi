from typing import List, Tuple
from board import *


class Player:
    """Player class for Reversi game.

    """
    def __init__(self, colour, name):
        self.colour = colour
        self.id = name

    def choose_move(self) -> Tuple[int, int, str]:
        move_x, move_y = -1, -1
        try:
            move_x = int(input("choose x_coordinate: "))
            move_y = int(input("choose y_coordinate: "))
        except ValueError:
            print("Invalid choice of move, please try again.")

        return move_x, move_y, self.colour

    def wins(self, score):
        print(self.id + " wins by " + str(score) + "!")


class CPUPlayer(Player):
    """
    CPU player for singleplayer mode.
    """
    def __init__(self, board):
        super().__init__("white", "CPU")
        self.board = board

    def choose_move(self):
        for x in range(self.board.dimension):
            for y in range(self.board.dimension):
                if self.board.is_valid_move(x, y, self.colour):
                    return x, y, self.colour



