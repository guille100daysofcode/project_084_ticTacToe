from functions import play, check_winner
from dicts import match_board


"""SETTING MATCH"""
positions_played = []
current_board = ""
is_game_on = True
turn = 0

while is_game_on:
    """DEFINES PLAYER TURN AND STATE OF THE BOARD"""
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    if turn == 0:
        print(match_board)
    else:
        match_board = current_board
    turn += 1

    if turn == 10:
        print("\n" * 20)
        print(current_board)
        print("DRAW. No Player wins.")
        is_game_on = False
        break

    """CHECKS USED POSITIONS AND MANAGES PLAYER'S PLAYS"""
    is_position_free = True
    while is_position_free:

        position = str(input(f"Player {player}, "
                             f"choose a board position for your piece (like '21', '33', etc...): "))
        if position not in positions_played:
            positions_played.append(position)
            is_position_free = False

            current_board = play(player, match_board, position)
            print("\n" * 20)
            print(current_board)
        else:
            print("\n" * 20)
            print(current_board)
            print("Already played. Try another position not currently in use:")

    """CHECKS WINNING COMBINATIONS"""
    if current_board.count("X") >= 3:
        if check_winner(current_board):
            winner = check_winner(current_board)
            print("\n" * 20)
            print(current_board)
            print(f"Player {winner}!!")
            break
