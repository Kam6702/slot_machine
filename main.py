import random
import config


class player(object):
    def __init__(self, bankroll):
        self.bankroll = int(bankroll)
        self.initial_bankroll = int(bankroll)

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


debug = player(100)
