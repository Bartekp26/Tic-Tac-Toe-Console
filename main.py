the_board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}


def print_board(board):
    print(f"""
        {board['7']} | {board['8']} | {board['9']}
        - + - + -
        {board['4']} | {board['5']} | {board['6']}
        - + - + -
        {board['1']} | {board['2']} | {board['3']}
    """)


def game():
    turn = 'X'
    count = 0

    while count < 10:
        print_board(the_board)

        try:
            move = int(input(f"[{turn}] Where would you like place your sign ( 1-9 ) ? "))
            if move < 1 or move > 9:
                print("You can enter only 1 to 9 numbers!")
                continue
        except ValueError:
            print("You can enter only 1 to 9 numbers!")
            continue

        if the_board[str(move)] == ' ':
            the_board[str(move)] = turn
            count += 1
        else:
            print("You can't place it here!")
            continue

        # if statement with all wining positions
        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ' or \
                    the_board['4'] == the_board['5'] == the_board['6'] != ' ' or \
                    the_board['7'] == the_board['8'] == the_board['9'] != ' ' or \
                    the_board['1'] == the_board['4'] == the_board['7'] != ' ' or \
                    the_board['2'] == the_board['5'] == the_board['8'] != ' ' or \
                    the_board['3'] == the_board['6'] == the_board['9'] != ' ' or \
                    the_board['1'] == the_board['5'] == the_board['9'] != ' ' or \
                    the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                print_board(the_board)
                print(f"{turn} won the game!")
                input()
                menu()

        # if statement with when it's a draw
        if count == 9:
            print_board(the_board)
            print("It's a draw")
            menu()

        # change turn after move
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'


def menu():
    restart = str(input("Would you like to play again? (y/n) ")).lower()

    if restart == 'y':
        for key in the_board:
            the_board[key] = ' '
        game()
    elif restart == 'n':
        exit()
    else:
        print("You can choose only 'y' - (yes) and 'n' - (no)!")
        menu()


game()
