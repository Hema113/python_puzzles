
def board(arr):
    for i in range(0, 9):
        if(i%3==0):
            print()
        print (" ", arr[i])
if __name__ == "__main__":
    arr =[1, 2, 3, 4, 5, 6, 7, 8, 9]
    board(arr)
