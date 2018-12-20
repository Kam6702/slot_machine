import engine, probability, config
from statistics import mean
import matplotlib.pyplot as plt

number_of_sessions = 500
trials = 100
bet = 1
initial_bankroll = 100
session_profits = []
session_wins = []
simulator = engine.player(initial_bankroll, 'auto')

print('Probabilities of each multiplier:')

for key in config.win_conditions:
    print(str(config.win_conditions[key]) + ' ' + str(
        probability.probability_of_multiplier(config.win_conditions, config.symbols, config.win_conditions[key])))
print('0 ' + str(probability.probability_of_loss(config.win_conditions, config.symbols, total_loss=True)))

for _ in range(number_of_sessions):
    session_win_count = 0
    for _ in range(trials):
        winnings = engine.calculate_winnings(engine.spin(), engine.place_bet(simulator, bet))
        engine.pay_winnings(simulator, winnings)
        if winnings > 0:
            session_win_count += 1
    profit = simulator.bankroll - initial_bankroll
    session_profits.append(profit)
    session_wins.append(session_win_count)
    simulator.bankroll = initial_bankroll

print('Profit: {}'.format(profit))
print('Average profit: ' + str(mean(session_profits)))
session = [i for i in range(1, number_of_sessions + 1)]
# plt.scatter(session, session_wins)
# plt.xlabel('Session')
# plt.ylabel('Number of Wins')
# plt.show()
