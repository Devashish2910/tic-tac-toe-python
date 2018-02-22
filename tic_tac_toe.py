import random


def display_board(board, space = 0):
    '''
    Function for displaing the board
    :param board: list of inputs from user
    :return: board
    '''
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- + - + - ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- + - + - ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n' * int(space))


def ask_for_marker():
    '''
    Function for setting 'X' or 'O' as marker
    :return: object containing both markers for both players
    '''

    marker = ''
    markers = {"player1": '', "player2": ''}

    while marker != 'X' and marker != 'O':
        marker = input("Player 1's Marker (O or X) =>")
        marker = marker.upper()

    if marker == 'O':
        markers['player1'] = marker
        markers['player2'] = 'X'
    else:
        markers['player1'] = marker
        markers['player2'] = 'O'

    print(f"Player-1 : {markers['player1']}")
    print(f"Player-2 : {markers['player2']}")
    print('\n')

    return markers


def place_maker(position, player, board):
    '''
    To make changes according to User input
    :param position: int - where to put marker
    :param player: player1 or player2 to get their marker
    :param board:
    :return: list - board with updated chanf=ges
    '''
    board[int(position)] = player
    return board


def win_check(board, player):
    '''
    Check player won or not!!
    :param board: list where to we are checking
    :param player: to get marker of the player
    :return: boolean
    '''
    return (
        board[1] == board[2] == board[3] == player or
        board[4] == board[5] == board[6] == player or
        board[7] == board[8] == board[9] == player or
        board[7] == board[4] == board[1] == player or
        board[8] == board[5] == board[2] == player or
        board[9] == board[6] == board[3] == player or
        board[7] == board[5] == board[3] == player or
        board[1] == board[5] == board[9] == player
    )


def space_on_place(place, board):
    return board[place] != 'X' and board[place] != 'O'


def space_in_board(board):
    is_empty = False
    i = 1
    while i < len(board):
        if board[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            is_empty = True
        i += 1
    return is_empty


def again_start():
    ip = input("Do you want to start again!! Yes or No ??")

    if ip == 'yes' or ip == 'YES' or ip == 'y' or ip == 'Y':
        print('\n' * 50)
        init()


def player1_turn(marker, board):
    """
    Take input and does calculations then either declare winner or pass on to player 2
    :param marker: to get player's marker
    :param board: to get status of the game board
    :return: --
    """
    marker_player = marker['player1']
    print(f"Player 1's ({marker_player}) Turn :-")

    if space_in_board(board):
        user_number = int(input("Enter Number Between 1 to 9: "))

        if user_number in range(1, 10):
            if space_on_place(user_number, board):
                board = place_maker(user_number, marker['player1'], board)
                if win_check(board, marker['player1']):
                    display_board(board)
                    print("Player 1 Won!!")
                    again_start()
                else:
                    display_board(board)
                    player2_turn(marker, board)
            else:
                print("Place Already Filled!!")
                player1_turn(marker, board)
        else:
            print("Wrong Input!!")
            player1_turn(marker, board)
    else:
        print("Match Drawn!!")
        again_start()


def player2_turn(marker, board):
    """
    Take input and does calculations then either declare winner or pass on to player 2
    :param marker: to get player's marker
    :param board: to get status of the game board
    :return: --
    """
    marker_player = marker['player2']
    print(f"Player 2's ({marker_player}) Turn :-")
    if space_in_board(board):
        user_number = int(input("Enter Number Between 1 to 9: "))

        if user_number in range(1, 10):

            if space_on_place(user_number, board):
                board = place_maker(user_number, marker['player2'], board)
                if win_check(board, marker['player2']):
                    display_board(board)
                    print("Player 2 Won!!")
                    again_start()
                else:
                    display_board(board)
                    player1_turn(marker, board)
            else:
                print("Place Already Filled.")
                player2_turn(marker, board)
        else:
            print("Wrong Input!!")
            player2_turn(marker, board)
    else:
        print("Match Drawn!!")
        again_start()


def init():
    print("Welcome to Tic-Tac-Toe:")
    print("\n")

    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    markers = ask_for_marker()

    if random.randint(0, 1) == 0:
        display_board(board)
        player1_turn(markers, board)
    else:
        display_board(board)
        player2_turn(markers, board)

init()