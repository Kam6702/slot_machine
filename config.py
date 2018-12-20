symbols = ['7', '<3', '$', '#', 'BAR', 'DOUBLE BAR', 'TRIPLE BAR']
win_conditions = {
    # Key represents win conditions, value represents multiple of bet returned
    # Each win condition must be a tuple with 3 values
    # Each multiple of bet returned must be a float
    # TODO: Can I use regex here to widen the possibilities?
    ('7', '7', '7'): 1.0,
    ('<3', '<3', '<3'): 1.5,
    ('$', '$', '$'): 2.0,
    ('#', '#', '#'): 2.5,
    ('BAR', 'BAR', 'BAR'): 5.0,
    ('DOUBLE BAR', 'DOUBLE BAR', 'DOUBLE BAR'): 10.0,
    ('TRIPLE BAR', 'TRIPLE BAR', 'TRIPLE BAR'): 30.0,
}
