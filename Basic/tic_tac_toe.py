from unittest.mock import Mock
import pytest


def tic_tac_toe_winner(board):
    return (
        (board[0] == board[1] == board[2])
        or (board[3] == board[4] == board[5])
        or (board[6] == board[7] == board[7])
        or (board[0] == board[3] == board[6])
        or (board[1] == board[4] == board[7])
        or (board[2] == board[5] == board[8])
        or (board[0] == board[4] == board[8])
        or (board[6] == board[4] == board[2])
    )


test_cases = {
    "True": ["X", "X", "X", "O", "X", "O", "X", "O", "O"],
    "True": ["O", "O", "O", "X", "O", "X", "O", "X", "X"],
    False: ["X", "X", "O", "X", "X", "O", "X", "X", "O"],
}


for expectation, board in test_cases.items():
    assert tic_tac_toe_winner(board) == expectation, f"Expected {expectation!r} for {board!r}"