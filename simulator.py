import engine, probability, config

# Simulator configuration
number_of_trials = 5
spins_per_trial = 50
bet_per_spin = 1
initial_bankroll = 100
payout_per_trial = []
profit_per_trial = []  # payout_per_trial - initial_bankroll
wins_per_trial = []  # List of number of spins that resulted in a win for each trial
average_payout_per_spin = []  # payout_per_trial / spins_per_trial
average_payout_per_win = []  # payout_per_trial / wins_per_trial
simulator = engine.player(initial_bankroll, 'auto')

print('Probabilities of each multiplier:')
print(probability.probability_of_all_multipliers(config.win_conditions, config.symbols))

for _ in range(number_of_trials):
    wins_for_trial = 0
    payout_for_trial = 0
    for _ in range(spins_per_trial):
        payout = engine.calculate_winnings(engine.spin(), engine.place_bet(simulator, bet_per_spin))
        engine.pay_winnings(simulator, payout)
        if payout > 0:
            wins_for_trial += 1
            payout_for_trial += payout
    probability.calculate_summary_statistics(wins_for_trial, payout_for_trial, number_of_trials, spins_per_trial,
                                             initial_bankroll)
    simulator.bankroll = initial_bankroll

