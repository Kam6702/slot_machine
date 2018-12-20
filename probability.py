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
