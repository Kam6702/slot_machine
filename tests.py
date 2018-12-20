import engine
import unittest
import config
import probability
import mock


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.player = engine.player(100, 'debug')

    def test_spin(self):
        a, b, c = engine.spin()
        assert a in config.symbols and b in config.symbols and c in config.symbols

    def test_calculate_winnings_win(self):
        assert engine.calculate_winnings(('BAR', 'BAR', 'BAR'), 2) == config.win_conditions[('BAR', 'BAR', 'BAR')] * 2

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


    def test_individual_symbol_probability(self):
        assert probability.individual_symbol_probability(2) == 0.5

    def test_probability_of_multiplier_exact(self):
        win_conditions = {
            ('X', 'X', 'X'): 1000.0,
        }
        symbols = ['X', 'Y']
        assert probability.probability_of_multiplier(win_conditions, symbols, 1000.0) == 0.125

    def test_probability_of_multiplier_not_exact(self):
        win_conditions = {
            ('1', '1', '1'): 10.0,
            ('2', '2', '2'): 1000.0
        }
        symbols = ['1', '2']
        assert probability.probability_of_multiplier(win_conditions, symbols, 5.0, exact_match=False) == 0.25

    def test_probability_of_loss_total_loss(self):
        win_conditions = {
            ('1', '1', '1'): 0.5,
            ('2', '2', '2'): 2
        }
        symbols = ['1', '2']
        assert probability.probability_of_loss(win_conditions, symbols) == 0.75

    def test_probability_of_loss_not_total_loss(self):
        win_conditions = {
            ('1', '1', '1'): 0.5,
            ('2', '2', '2'): 2
        }
        symbols = ['1', '2']
        assert probability.probability_of_loss(win_conditions, symbols, total_loss=False) == 0.875

    def test_load_save_game(self):
        self.player.bankroll = engine.load_bankroll(self.player)
        assert self.player.bankroll == 50

    # TODO add test for save game

    def tearDown(self):
        del self.player
