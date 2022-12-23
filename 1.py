screen = ' ' * 12

tokens = {'@' : 10, '$' : 50, '&' : 200, '*' : 1000}

def count_token():
    sum_combo = 0
    for token, value in tokens.items():
        sum_combo += check_win(token, value)
    return sum_combo

def check_win(token, value):
    win_counter = 0
    for i in range(3):
        if screen[i] == screen[i+1] == screen[i+2] == screen[i+3] == token:
            win_counter += 1
    for i in range(4):
        if screen[i] == screen[i+4] == screen[i+8] == token:
            win_counter += 1
    return win_counter * value

def generate_combos():
    global screen
    for i in screen:
        screen = choice(tokens)
