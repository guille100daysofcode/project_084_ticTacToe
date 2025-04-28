from dicts import play_positions, winning_positions


def play(player, board, position):
    symbol = ""
    if player == "X":
        symbol = "X"
    elif player == "O":
        symbol = "O"

    list_match_board = list(board)
    list_match_board[play_positions[position]] = symbol
    updated_match_board = "".join(list_match_board)

    return updated_match_board


def check_winner(board):
    for comb in winning_positions:
        if board[comb[0]] == board[comb[1]] and board[comb[1]] == board[comb[2]]:
            if board[comb[0]] == "X" or board[comb[0]] == "O":
                winner = board[comb[0]]
                return winner
            else:
                return False
