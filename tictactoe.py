import random
import math
import time


def make_board():
    board = []
    for i in range(9):
        board.append(' ')
    return board


def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def print_board_nums():
    number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')


def make_move(board, square, letter):
    if board[square] == ' ':
        board[square] = letter
        return True
    return False


def check_winner(board, letter):
    # Check rows
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        if all([s == letter for s in row]):
            return True

    for i in range(3):
        column = [board[i + j * 3] for j in range(3)]
        if all([s == letter for s in column]):
            return True

    diagonal1 = [board[i] for i in [0, 4, 8]]
    if all([s == letter for s in diagonal1]):
        return True
    diagonal2 = [board[i] for i in [2, 4, 6]]
    if all([s == letter for s in diagonal2]):
        return True

    return False


def has_empty_squares(board):
    return ' ' in board


def num_empty_squares(board):
    return board.count(' ')


def available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]


def play(print_game=True):
    board = make_board()
    current_winner = None
    letter = 'X'

    if print_game:
        print_board_nums()

    while has_empty_squares(board):
        if letter == 'O':
            square = get_human_move(board, letter)
        else:
            square = computer_move(board, letter)

        if make_move(board, square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                print_board(board)
                print('')

            if check_winner(board, letter):
                if print_game:
                    print(letter + ' wins!')
                current_winner = letter
                break
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game and not current_winner:
        print('No winner!')


def get_human_move(board, letter):
    valid_square = False
    val = None
    while not valid_square:
        square = input(letter + ' Enter your moves between (0-8): ')
        try:
            val = int(square)
            if val not in available_moves(board):
                raise ValueError
            valid_square = True
        except ValueError:
            print('Invalid move. Try again.')
    return val


def computer_move(board, letter):
    if len(available_moves(board)) == 9:
        square = random.choice(available_moves(board))
    else:
        square = minimax(board, letter)['position']
    return square


def minimax(board, player):
    max_player = 'X'
    human_player = 'O' if player == 'X' else 'X'

    if check_winner(board, human_player):
        return {'position': None, 'score': 1 * (num_empty_squares(board) + 1) if human_player == max_player else -1 * (
                num_empty_squares(board) + 1)}
    elif not has_empty_squares(board):
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in available_moves(board):
        new_board = board.copy()
        make_move(new_board, possible_move, player)
        sim_score = minimax(new_board, human_player)

        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    return best


play()
