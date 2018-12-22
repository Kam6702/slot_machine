
def individual_symbol_probability(number_of_symbols):
    return float(1 / number_of_symbols)


def probability_of_multiplier(win_conditions, symbols, multiplier, exact_match=True):
    # Expects win_conditions as dictionary, symbols as list, and multiplier as float
    # When exact_match is set to True, the logic will only consider returns of the exact specified multiplier
    # When exact_match is set to False, the logic will consider returns of the specified multiplier or greater
    scenarios = 0
    for key in win_conditions:
        if exact_match:
            if win_conditions[key] == multiplier:
                scenarios += 1
        else:
            if win_conditions[key] >= multiplier:
                scenarios += 1
    return round(float(scenarios) * individual_symbol_probability(len(symbols)) ** 3.0, 4)


def probability_of_loss(win_conditions, symbols, total_loss=True):
    # Expects win_conditions as dictionary and symbols as list
    # When total_loss is set to False, the logic will consider any return below a 1.0 multiplier to be a loss
    # When total_loss is set to True, the logic will only consider a return of 0.0 to be a loss
    if total_loss:
        return round(1.0 - probability_of_multiplier(win_conditions, symbols, 0.0, exact_match=False), 4)
    else:
        probability_greater_than_0 = probability_of_multiplier(win_conditions, symbols, 0.0, exact_match=False)
        probability_greater_than_1 = probability_of_multiplier(win_conditions, symbols, 0.9999, exact_match=False)
        return 1.0 - (probability_greater_than_0 - probability_greater_than_1)


def calculate_summary_statistics(wins_for_trial, payout_for_trial, number_of_trials, spins_per_trial,
                                 initial_bankroll):  # FIXME Fix refactoring
    global profit_per_trial, wins_per_trial, average_payout_per_spin, average_payout_per_win
    profit_for_trial = simulator.simulator.bankroll - initial_bankroll
    profit_per_trial.append(profit_for_trial)
    wins_per_trial.append(wins_for_trial)
    payout_per_trial.append(payout_for_trial)
    average_payout_per_spin.append(payout_for_trial / spins_per_trial)
    if wins_for_trial != 0:
        average_payout_per_win.append(payout_for_trial / wins_for_trial)
    if wins_for_trial == 0:
        average_payout_per_win.append(0)


def print_summary_statistics():
    pass


def probability_of_all_multipliers(win_conditions, symbols):
    # Accepts win_conditions as dictionary and symbols as list
    probabilities = {}
    for key in win_conditions:
        probabilities[win_conditions[key]] = probability_of_multiplier(win_conditions, symbols, win_conditions[key])
    probabilities[0.0] = probability_of_loss(win_conditions, symbols, total_loss=True)
    return probabilities


def expected_payout_of_trial(probabilities_of_all_multipliers, bet, spins_per_trial):
    # Assumes consistent bet per spin
    expected_multiplier = 0
    expected_payout = 0
    for key in probabilities_of_all_multipliers:
        expected_multiplier += key * probabilities_of_all_multipliers[key]
    expected_payout = bet * expected_multiplier
    return expected_payout * spins_per_trial


def expected_profit_of_trial(expected_payout_of_trial, bet, spins_per_trial):
    return expected_payout_of_trial - (bet * spins_per_trial)
