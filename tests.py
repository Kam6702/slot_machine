import main
import unittest
import config


class TestSuite(unittest.TestCase):
    def test_spin(self):
        a, b, c = main.spin()
        assert a in config.symbols and b in config.symbols and c in config.symbols

    def test_win_conditions(self):
        assert config.win_conditions[('BAR', 'BAR', 'BAR')] == 5.0

    def test_calculate_winnings_win(self):
        assert main.calculate_winnings(('BAR', 'BAR', 'BAR'), 2) == 10.0

    def test_calculate_winnings_lost(self):
        assert main.calculate_winnings(('BAR', 'BAR', '7'), 2) == 0
