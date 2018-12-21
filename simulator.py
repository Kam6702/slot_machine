import engine, probability, config
from statistics import mean
import matplotlib.pyplot as plt

number_of_trials = 5
spins_per_trial = 50
bet_per_spin = 1
initial_bankroll = 100
payout_per_trial = []
profits_per_trial = []  # payout_per_trial - initial_bankroll
wins_per_trial = []  # List of number of spins that resulted in a win for each trial
average_payout_per_spin = []  # payout_per_trial / spins_per_trial
average_payout_per_win = []  # payout_per_trial / wins_per_trial
simulator = engine.player(initial_bankroll, 'auto')


def calculate_summary_statistics(wins_for_trial, payout_for_trial, number_of_trials, spins_per_trial, initial_bankroll):
    global profits_per_trial, wins_per_trial, average_payout_per_spin, average_payout_per_win
    profit_for_trial = simulator.bankroll - initial_bankroll
    profits_per_trial.append(profit_for_trial)
    wins_per_trial.append(wins_for_trial)
    payout_per_trial.append(payout_for_trial)
    average_payout_per_spin.append(payout_for_trial / spins_per_trial)
    if wins_for_trial != 0:
        average_payout_per_win.append(payout_for_trial / wins_for_trial)
    if wins_for_trial == 0:
        average_payout_per_win.append(0)


def print_summary_statistics():
    pass

print('Probabilities of each multiplier:')

for key in config.win_conditions:
    print(str(config.win_conditions[key]) + ' ' + str(
        probability.probability_of_multiplier(config.win_conditions, config.symbols, config.win_conditions[key])))
print('0 ' + str(probability.probability_of_loss(config.win_conditions, config.symbols, total_loss=True)))

for _ in range(number_of_trials):
    wins_for_trial = 0
    payout_for_trial = 0
    for _ in range(spins_per_trial):
        payout = engine.calculate_winnings(engine.spin(), engine.place_bet(simulator, bet_per_spin))
        engine.pay_winnings(simulator, payout)
        if payout > 0:
            wins_for_trial += 1
            payout_for_trial += payout
    calculate_summary_statistics(wins_for_trial, payout_for_trial, number_of_trials, spins_per_trial, initial_bankroll)
    simulator.bankroll = initial_bankroll

