import random

board = [x for x in range(1, 10)]
available = [x for x in range(1, 10)]
is_win = False
winner = 0

def draw_field():
    global board
    l = 0
    for x in range(3):
        print(f'-------------\n'
              f'| {board[l]} | {board[l+1]} | {board[l+2]} |')
        l+=3
    print(f'-------------\n')

def check_win():
    global is_win, board, winner
    if (board[0] == board[4] == board[8] == 'x') or \
        (board[2] == board[4] == board[6] == 'x') or \
        (board[0] == board[1] == board[2] == 'x') or \
        (board[3] == board[4] == board[5] == 'x') or \
        (board[6] == board[7] == board[8] == 'x') or \
        (board[0] == board[3] == board[6] == 'x') or \
        (board[1] == board[4] == board[7] == 'x') or \
        (board[2] == board[5] == board[8] == 'x'):
            is_win = True
            winner = 2
    if (board[0] == board[4] == board[8] == 'o') or \
        (board[2] == board[4] == board[6] == 'o') or \
        (board[0] == board[1] == board[2] == 'o') or \
        (board[3] == board[4] == board[5] == 'o') or \
        (board[6] == board[7] == board[8] == 'o') or \
        (board[0] == board[3] == board[6] == 'o') or \
        (board[1] == board[4] == board[7] == 'o') or \
        (board[2] == board[5] == board[8] == 'o'):
            is_win = True
            winner = 1
    elif len(available) == 0:
        is_win = True
        winner = 0

def require_character():
    global available, board
    #print(available)
    if len(available) == 0:
        return None
    user_input = 0
    validated = False
    while not validated:
        user_input = input("Enter check: ")
        try:
            user_input = int(user_input)
            if user_input in available:
                validated = True
        except ValueError as ve:
            pass
    available.remove(int(user_input))
    board[int(user_input)-1] = 'x'

def bot_turn():
    global available, board
    if len(available) == 0:
        return False
    rows = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]

    # checking horizontal
    for row in rows:
        if board[row[0]] == board[row[1]] and board[row[2]] in available:
            available.remove(board[row[2]])
            board[row[2]] = 'o'
            return 0

        elif board[row[1]] == board[row[2]] and board[row[0]] in available:
            available.remove(board[row[0]])
            board[row[0]] = 'o'
            return 0

        elif board[row[0]] == board[row[2]] and board[row[1]] in available:
            available.remove(board[row[1]])
            board[row[1]] = 'o'
            return 0

    # checking vertical
    for row in zip(rows[0], rows[1], rows[2]):
        if board[row[0]] == board[row[1]] and board[row[2]] in available:
            available.remove(board[row[2]])
            board[row[2]] = 'o'
            return 0

        elif board[row[1]] == board[row[2]] and board[row[0]] in available:
            available.remove(board[row[0]])
            board[row[0]] = 'o'
            return 0

        elif board[row[0]] == board[row[2]] and board[row[1]] in available:
            available.remove(board[row[1]])
            board[row[1]] = 'o'
            return 0

    # checking diagonal
    if board[rows[0][0]] == board[rows[1][1]] and board[rows[2][2]] in available:
        available.remove(board[rows[2][2]])
        board[rows[2][2]] = 'o'
        return 0
    elif board[rows[0][0]] == board[rows[2][2]] and board[rows[1][1]] in available:
        available.remove(board[rows[1][1]])
        board[rows[1][1]] = 'o'
        return 0
    elif board[rows[2][2]] == board[rows[1][1]] and board[rows[0][0]] in available:
        available.remove(board[rows[0][0]])
        board[rows[0][0]] = 'o'
        return 0
    elif board[rows[0][2]] == board[rows[1][1]] and board[rows[2][0]] in available:
        available.remove(board[rows[2][0]])
        board[rows[2][0]] = 'o'
        return 0
    elif board[rows[0][2]] == board[rows[2][0]] and board[rows[1][1]] in available:
        available.remove(board[rows[1][1]])
        board[rows[1][1]] = 'o'
        return 0
    elif board[rows[2][0]] == board[rows[1][1]] and board[rows[0][2]] in available:
        available.remove(board[rows[0][2]])
        board[rows[0][2]] = 'o'
        return 0
    else:
        check = random.choice(available)
        available.remove(check)
        board[check-1] = 'o'

def main():
    while not is_win:
        draw_field()
        require_character()
        bot_turn()
        check_win()
    draw_field()
    if winner == 1:
        print("The bot won")
    elif winner == 2:
        print("You won")
    elif winner == 0:
        print("It's draw")
    else:
        print("Something went wrong")

if __name__ == '__main__':
    main()