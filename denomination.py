# Program for find changes for given amount
# Find  and retrurn the change denomination
def denomination(amount):
    result = []
    denomination = [2000, 500 ,200 ,100 ,50 ,20 ,10 ,5 ,2 ,1]
    for i in range(0, len(denomination)):
        if amount >= denomination[i] and amount > 0:
            rs=amount % denomination[i]
            rs_count=int(amount/denomination[i])
            result.append([denomination[i], rs_count])
            amount = rs
    return result

# Main
if __name__ == "__main__":
    amount = int(input("Enter the amount>>>"))
    print(denomination(amount))
