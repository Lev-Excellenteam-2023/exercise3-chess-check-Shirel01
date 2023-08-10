import pytest
from pytest import fixtures
import chess_engine
from Piece import Knight, Piece
from enums import Player

import chess_engine
from Piece import Knight
from enums import Player
import enums
from chess_engine import game_state
from unittest.mock import Mock
import Piece

@pytest --fixtures
def _test_get_valid_piece_moves(game):

    game = chess_engine.game_state()
    game.board = [[Player.EMPTY] * 8 for _ in range(8)]
    game.board = [Piece.Knight('k', 3, 4, 'white'), Piece.Piece('pawn', 1, 5, 'black'),
                        Piece.Piece('pawn', 4, 2, 'black'), Piece.Piece('pawn', 5, 3, 'black'),
                        Piece.Piece('rook', 1, 3, 'black'), Piece.Piece('knight', 2, 2, 'black'),
                        Piece.Piece('knight', 5, 5, 'black'), Piece.Piece('pawn', 2, 6, 'black'),
                        Piece.Piece('pawn', 4, 6, 'black')]
    peaceful_moves = game.get_piece(3, 4).get_valid_piece_moves(game)
    expected_moves = {(1, 3), (4, 2), (4, 6), (5, 3), (5, 5)}














