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

    name1 = input("Please enter name of Player 1: ")
    player1 = Player("black", name1)

    if num_players > 1:
        name2 = input("Please enter name of Player 2: ")
        player2 = Player("white", name2)
    else:
        player2 = CPUPlayer("white", "CPU")

    while True:
        if board.turn == "p1":
            if not board.valid_move_exists("black"):
                print("No valid moves!")
                board.turn == "p2"
                continue
            board.get_move(player1)
            board.display_board()
            board.next_turn()
        else:
            if not board.valid_move_exists("white"):
                print("No valid moves!")
                board.turn == "p1"
                continue
            board.get_move(player2)
            board.display_board()
            board.next_turn()























if __name__ == '__main__':
    main()

