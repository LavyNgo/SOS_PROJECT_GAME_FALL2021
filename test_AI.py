import unittest
import sos2


class TestSos(unittest.TestCase):

    # Checking the board dimension
    def test_board(self):
        Board = SOS.board
        size = SOS.board_size
        self.assertEqual(len(Board), size)

    # This test is used to check the function isFull returns True when the board has no empty cell left
    def test_isFull(self):
        full = SOS.isfull()
        self.assertEqual(full, True)

    # This test is used to check the setting is computer when the player clicks on computer button for blue player
    def test_Bluecomputer(self):
        mode = SOS.Mode_1.get()
        self.assertEqual(mode, 'Computer')

    # This test is used to check the setting is computer when the player clicks on computer button for blue player
    def test_Redcomputer(self):
        mode = SOS.Mode_2.get()
        self.assertEqual(mode, 'Computer')
