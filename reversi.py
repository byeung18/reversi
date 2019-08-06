from player import *
from board import *


def main():
    """
    Reversi game interface.
    :return:
    """
    num_players = 0
    while num_players != 1 and num_players != 2:
        try:
            num_players = int(input("How many players? (1 or 2): "))
        except ValueError:
            print("Invalid number of players, please enter 1 or 2")

    board_size = 0
    while board_size < 1 or board_size % 2 != 0:
        try:
            board_size = int(input("What size board?: "))
        except ValueError:
            print("Invalid board size, please enter integer")

    board = Board(board_size)
    board.display_board()




















if __name__ == '__main__':
    main()

