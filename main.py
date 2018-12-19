import random
import config


def spin():
    return (random.choice(config.symbols), random.choice(config.symbols), random.choice(config.symbols))


def calculate_winnings(spin_results, bet):
    try:
        multiplier = config.win_conditions[spin_results]
        return multiplier * bet
    except KeyError:
        return 0

