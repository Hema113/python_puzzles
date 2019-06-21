def deposit(in_put):
    current_bal = 0
    while True:
    #in_put = input("Enter the amount>>>").split()
        if not in_put:
            break;

        inp = int(in_put[1])
        if in_put[0] == "d":
            current_bal += inp
        elif in_put[0] == "w":
            current_bal -= inp

    return current_bal


if __name__ == "__main__":
    in_put = input("Enter the amount>>>").split()
    print(deposit(in_put))
