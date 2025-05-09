print("Welcome to the Game Tic Tac Toe")
print("Full Game in Console Command")

def play_game():
    win_pos = [[11,12,13],[21,22,23],[31,32,32],[11,22,33],[13,22,31],[11,21,32],[12,22,32],[13,23,33]]
    board = {
        11: ' ', 12: ' ', 13: ' ',
        21: ' ', 22: ' ', 23: ' ',
        31: ' ', 32: ' ', 33: ' '
    }
    def print_board():
        print(f" {board[11]} | {board[12]} | {board[13]} ")
        print("-----------")
        print(f" {board[21]} | {board[22]} | {board[23]} ")
        print("-----------")
        print(f" {board[31]} | {board[32]} | {board[33]} ")

    def is_winning(moves):
        for combo in win_pos:
            if all(pos in moves for pos in combo):
                return True
        return False

    count = 1
    x = []
    y = []
    flag = 0
    print("\nNew game started!")
    print("Positions are numbered as:")
    print(" 11 | 12 | 13 ")
    print("-----------")
    print(" 21 | 22 | 23 ")
    print("-----------")
    print(" 31 | 32 | 33 \n")
    while count<10:
        if count%2!=0:
            f = 1
            while f:
                try:
                    n = int(input("Player 1 enter the value: "))
                    if n not in board:
                        print("Invalid position! Enter a value between 11-33.")
                    elif n in x or n in y:
                        print("enter correct number")
                    else:
                        board[n] = 'X'
                        x.append(n)
                        break
                except ValueError:
                    print("Please enter a valid number!")
            print_board()
            if is_winning(x):
                print("Player 1 (X) wins!")
                flag = 1
                break
        else:
            f = 1
            while f:
                try:
                    n = int(input("Player 2 enter the value: "))
                    if n not in board:
                        print("Invalid position! Enter a value between 11-33.")
                    elif n in x or n in y:
                        print("enter correct number")
                    else:
                        board[n] = 'Y'
                        y.append(n)
                        break
                except ValueError:
                    print("Please enter a valid number!")
            print_board()
            if is_winning(y):
                print("Player 2 (Y) wins!")
                flag = 1
                break
        count+=1
    if flag == 0:
        print("The match is draw")

while True:
    play_game()
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing! Goodbye!")
        break
