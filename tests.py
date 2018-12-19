import engine
import unittest
import config


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.player = engine.player(100)

    def test_spin(self):
        a, b, c = engine.spin()
        assert a in config.symbols and b in config.symbols and c in config.symbols

    def test_win_conditions(self):
        assert config.win_conditions[('BAR', 'BAR', 'BAR')] == 5.0

    def test_calculate_winnings_win(self):
        assert engine.calculate_winnings(('BAR', 'BAR', 'BAR'), 2) == 10.0

    def test_calculate_winnings_lost(self):
        assert engine.calculate_winnings(('BAR', 'BAR', '7'), 2) == 0

    def test_subtract_bet_from_bankroll(self):
        engine.place_bet(self.player, 20)
        assert self.player.bankroll == 80
        self.player.bankroll += 20  # Reset player object after the test

    def test_add_winnings_to_bankroll(self):
        engine.pay_winnings(self.player, 100)
        assert self.player.bankroll == 200
        self.player.bankroll -= 100  # Reset player object after the test

    def test_create_new_player(self):
        debug = engine.create_new_player('debug')
        try:
            debug
            player_created = True
        except NameError:
            player_created = False
        assert player_created
        del debug

    def tearDown(self):
        del self.player
