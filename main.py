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


game()
