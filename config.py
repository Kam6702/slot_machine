symbols = ['7', '<3', '$', '#', 'BAR', 'DOUBLE BAR', 'TRIPLE BAR']
win_conditions = {
    # Key represents win conditions, value represents multiple of bet returned
    ('7', '7', '7'): 1.0,
    ('<3', '<3', '<3'): 1.5,
    ('$', '$', '$'): 2.0,
    ('#', '#', '#'): 2.5,
    ('BAR', 'BAR', 'BAR'): 5.0,
    ('DOUBLE BAR', 'DOUBLE BAR', 'DOUBLE BAR'): 10.0,
    ('TRIPLE BAR', 'TRIPLE BAR', 'TRIPLE BAR'): 30.0,
}
