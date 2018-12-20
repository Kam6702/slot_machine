import random
import config
import pickle
import os

class player(object):
    def __init__(self, bankroll, name):
        self.bankroll = int(bankroll)
        self.initial_bankroll = int(bankroll)
        self.name = name


def spin():
    return (random.choice(config.symbols), random.choice(config.symbols), random.choice(config.symbols))


def calculate_winnings(spin_results, bet):
    try:
        multiplier = config.win_conditions[spin_results]
        return multiplier * bet
    except KeyError:
        return 0


def place_bet(player, bet):
    try:
        bet = int(bet)
        if player.bankroll - bet >= 0 and bet > 0:
            player.bankroll -= bet
            return bet
        else:
            place_bet(player, input('Please enter a valid bet: '))
    except (TypeError, ValueError):
        place_bet(player, input('Please enter a valid bet: '))


def pay_winnings(player, winnings):
    player.bankroll += winnings


def create_new_player(player_name):
    new_player = player(100, player_name)
    return new_player


def save_bankroll(player_object):
    file = player_object.name + '.dat'  # TODO Create a saved games directory
    with open(file, 'wb') as save_game:
        pickle.dump(player_object.bankroll, save_game)


def load_bankroll(player_object):
    file = player_object.name + '.dat'
    with open(file, 'rb') as load_game:
        return pickle.load(load_game)
