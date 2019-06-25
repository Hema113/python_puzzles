def deposit():
    current_bal = 0
    while True:
        in_put = input("Enter the amount>>>").split()
        if not in_put:
            break;

        amount = int(in_put[1])
        if in_put[0] == "d" or in_put[0] == "D":
            current_bal += amount
        elif in_put[0] == "w" or in_put[0] == "W":
            current_bal -= amount
        #elif in_put == 'exit':
        #    break

    return current_bal


if __name__ == "__main__":
    print("Balance>>>>",deposit())
