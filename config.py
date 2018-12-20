symbols = ['7', '<3', '$', '#', 'BAR', 'DOUBLE BAR', 'TRIPLE BAR']
win_conditions = {
    # Key represents win conditions, value represents multiple of bet returned
    # Each win condition must be a tuple with 3 values
    # Each multiple of bet returned must be a float
    ('7', '7', '7'): 20.0,
    ('<3', '<3', '<3'): 40.0,
    ('$', '$', '$'): 60.0,
    ('#', '#', '#'): 100.0,
    ('BAR', 'BAR', 'BAR'): 500.0,
    ('DOUBLE BAR', 'DOUBLE BAR', 'DOUBLE BAR'): 1500.0,
    ('TRIPLE BAR', 'TRIPLE BAR', 'TRIPLE BAR'): 10000.0
}
