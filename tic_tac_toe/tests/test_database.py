import pytest
from os import close, unlink
from tempfile import mkstemp
from itertools import count
from sqlalchemy import create_engine
from unittest.mock import Mock

from tic_tac_toe.database import winner, metadata, history


User = Mock(query=Mock(all=Mock(return_value=[Mock(id=7, first_name="Guido", last_name="van Rossum")])))


@pytest.fixture
def connection_mock():
    return lambda moves: Mock(
        execute=Mock(return_value=[(int(position), symbol) for position, symbol in zip(moves[::2], moves[1::2])])
    )


def test_3x_in_a_column(connection_mock):
    response = winner(connection_mock("4X1O5X3O2X6O8X"), None)
    assert response.json()["winner"] == "X"


@pytest.mark.parametrize(
    "board, expected",
    [("3O0X4O1X7O2X", "X"), ("0O3X2O4X7O5X", "X"), ("0O6X2O7X3O8X", "X"), ("4O1X5O3X2O6X8O", "O")],
)
def test_3x_in_a_row(connection_mock, expected, board):
    response = winner(connection_mock(board), None)
    assert response.json()["winner"] == expected


def test_create_board_from_moves(connection_mock, monkeypatch):
    monkeypatch.setattr("tic_tac_toe.database.tic_tac_toe_winner", lambda board: board)
    response = winner(connection_mock("4X1O5X3O2X6O8X"), None)
    print("Response type: ", type(response))
    print("Assertion right side type: ", type(" OXOXXO X"))
    print("Are they equal?")
    print(f"assert response:", response.json())
    assert response == " OXOXXO X"
