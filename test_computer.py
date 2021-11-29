import unittest
import sos


class TestSos(unittest.TestCase):

    # Checking the board size
    def test_board(self):
        test_board = sos.board
        test_size = sos.board_size
        self.assertEqual(len(test_board), test_size)

    # Checking S in row 0, column 1
    def test_position_human(self):
        test_board = sos.board
        self.assertEqual(test_board[0][1], "S")


    # Choosing the computer mode for blue player
    def test_blue_player_computer(self):
        test_b = sos.blueMode.get()
        self.assertEqual(test_b, "Computer")


