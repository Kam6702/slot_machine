import random
import config


def spin():
    spin_results = []
    for i in range(3):
        spin_results.append(random.choice(config.symbols))
    return spin_results


def calculate_winnings(spin_results, bet):
    try:
        multiplier = config.win_conditions[spin_results]
        return multiplier * bet
    except KeyError:
        return 0
