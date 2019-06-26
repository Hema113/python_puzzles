# Tic_tac_Toe game
# Function for specify board size and winning possibles
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_possible = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# Function for print board
    def draw():
        print(arr[0], arr[1], arr[2])
        print(arr[3], arr[4], arr[5])
        print(arr[6], arr[7], arr[8])
        print()

# Player 1
    def player1():
        n = choose_number()
        if arr[n] == "X" or arr[n] == "O":
            print("\nYou can't go there. Try again")
            player1()
        else:
            arr[n] = "X"

# Player 2
    def player2():
        n = choose_number()
        if arr[n] == "X" or arr[n] == "O":
            print("\nYou can't go there. Try again")
            player2()
        else:
            arr[n] = "O"

# Function for choose number and place input X or O in that board
    def choose_number():
        while True:
            while True:
                get_ip = input()
                try:
                    get_ip = int(get_ip)
                    get_ip -= 1
                    if get_ip in range(0, 9):
                        return get_ip
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

# Checking winnin places depends on the user input
    def check_board():
        count = 0
        for get_ip in win_possible:
            if arr[get_ip[0]] == arr[get_ip[1]] == arr[get_ip[2]] == "X":
                print("Player 1 Wins!\n")
                return True

            if arr[get_ip[0]] == arr[get_ip[1]] == arr[get_ip[2]] == "O":
                print("Player 2 Wins!\n")
                return True

        for get_ip in range(9):
            if arr[get_ip] == "X" or arr[get_ip] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        player1()
        print()

        draw()
        end = check_board()

        if end == True:
            break
        print("Player 2 choose where to place a nought")
        player2()
        print()

main()
