import engine
import time


def start_menu():
    print('Create New Player: N \nUse Existing Player: E')
    command = input('Enter a command: ').upper()
    player = engine.create_new_player(input('Enter a name for your player: '))
    if command == 'E':
        try:
            player.bankroll = engine.load_bankroll(player)
        except FileNotFoundError:
            print('This player does not exist')
            start_menu()
    return player


active_game = True

print('Welcome to the Python Slot Machine')
active_player = start_menu()
while active_game == True:
    print('Credit Balance: {}'.format(active_player.bankroll))
    command = input('Enter your bet to spin or X to exit the game: ')  # TODO Make this upper case
    if command == 'X':
        active_game = False
        break
    else:
        engine.place_bet(active_player, command)
        print('Spinning...')
        spin_results = engine.spin()
        winnings = engine.calculate_winnings(spin_results, command)
        print(spin_results)
        print('You\'ve won {} credits.'.format(winnings))
        engine.pay_winnings(active_player, winnings)

engine.save_bankroll(active_player)
