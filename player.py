from typing import List, Tuple


class Player:
    """Player class for Reversi game.

    """
    def __init__(self, colour, name):
        self.colour = colour
        self.id = name

    def choose_move(self) -> Tuple[int, int, str]:
        try:
            move_x = int(input("choose x_coordinate: "))
            move_y = int(input("choose y_coordinate: "))
        except ValueError:
            print("Invalid choice of move, please try again.")

        return move_x, move_y, self.colour



