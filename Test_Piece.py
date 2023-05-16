import unittest
from Piece import Knight
from enums import Player
import enums
from chess_engine import game_state
from unittest.mock import Mock
import Piece


def board(pieces):
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    for piece in pieces:
        row = piece.get_row_number()
        col = piece.get_col_number()
        board[row][col] = piece

    return board


class TestKnight(unittest.TestCase):
    def test_get_valid_peaceful_moves_empty_board(self):
        knight = Piece.Knight('k', 3, 4, Player.PLAYER_1)
        game = Mock()
        game.get_piece.return_value = Player.EMPTY
        peaceful_moves = knight.get_valid_peaceful_moves(game)
        expected_moves = {(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)}
        assert set(peaceful_moves) == expected_moves  # return a set because the order doesnt matter

    def test_get_valid_peaceful_moves_almost_empty_board(self):
        knight = Piece.Knight('k', 3, 4, Player.PLAYER_1)
        # Create a mock game object with an occupied square
        game = Mock()
        game.get_piece.side_effect = lambda row, col: Player.EMPTY if (row, col) != (2, 6) else Player.PLAYER_2
        peaceful_moves = knight.get_valid_peaceful_moves(game)
        expected_moves = {(1, 3), (1, 5), (2, 2), (4, 2), (4, 6), (5, 3), (5, 5)}
        assert set(peaceful_moves) == expected_moves


    def test_get_valid_peaceful_moves_all_squares_occupied(self):
        knight = Piece.Knight('k', 3, 4, Player.PLAYER_1)
        game = Mock()
        game.get_piece.return_value = Player.PLAYER_2  # Simulating all squares occupied by another player
        peaceful_moves = knight.get_valid_peaceful_moves(game)
        expected_moves = []
        assert peaceful_moves == expected_moves

    '''def test_get_valid_piece_takes(self):
        knight = Piece.Knight('k', 3, 4, Player.PLAYER_1)
        game = Mock()
        game.get_piece.return_value = Player.Player_2
        takes_moves='''

    def test_get_valid_piece_takes_occupied_squares(self):
        game = Mock()
        game.board = board([Piece.Knight('k', 3, 4, 'white'), Piece.Piece('k', 2, 2, 'black'),
                            Piece.Piece('r', 4, 2, 'black'), Piece.Piece('k', 5, 3, 'black'),
                            Piece.Piece('k', 1, 5, 'white')])
        mock_get_piece = Mock(side_effect=lambda row, col: game.board[row][col] if 0 <= row < 8 and 0 <= col < 8 else None)
        game.get_piece = mock_get_piece
        mock_is_valid = Mock(side_effect=lambda row, col: game.get_piece(row, col) is not None and game.get_piece(row, col) != Player.EMPTY)
        game.is_valid_piece = mock_is_valid
        peaceful_moves = game.get_piece(3, 4).get_valid_piece_takes(game) # The get_valid_piece_takes method is called on the piece at position (3, 4) using game.get_piece(3, 4).
        expected_moves = {(2, 2), (4, 2), (5, 3)}
        assert set(peaceful_moves) == expected_moves








