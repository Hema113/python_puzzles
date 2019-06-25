# program for caiculateing bank balance

def deposit():
    current_bal = 0
    while True:
        in_put = input("Enter the amount>>>").split()
        if not in_put: #----> if input is empty then exit from the loop-
            break;

        amount = int(in_put[1]) # Convert user input string to int it takes the list[1] value it means 100
        if in_put[0] == "d" or in_put[0] == "D":
            current_bal += amount #---->Deposit amt calcultion
        elif in_put[0] == "w" or in_put[0] == "W":
            current_bal -= amount #------> Withdraw amt calculation
        #elif in_put == 'exit':
        #    break

    return current_bal


if __name__ == "__main__":
    print("Balance>>>>",deposit())
