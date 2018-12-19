def individual_symbol_probability(number_of_symbols):
    return float(1 / number_of_symbols)


def probability_of_multiplier(win_conditions, symbols, multiplier, exact_match=True):
    # Expects win_conditions as dictionary, symbols as list, and multiplier as float
    # If exact_match is set to False, the logic will consider win-scenarios above the target multiplier
    scenarios = 0
    for key in win_conditions:
        if exact_match:
            if win_conditions[key] == multiplier:
                scenarios += 1
        else:
            if win_conditions[key] >= multiplier:
                scenarios += 1
    return round(float(scenarios) * individual_symbol_probability(len(symbols)) ** 3.0, 4)
