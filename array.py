# program for createing 2D array
# createing 2D array
def array_1(row ,col):
    #array = [[0]  * col] *row
    array =[[0 for col in range(col)]for row in range(row)] #-----> calculteing rows and columns

    for i in range(row):
        for j in range(col):
            array[i][j] = i * j
    return array

# Main
if __name__ == "__main__":
    #x = 3
    #y = 5
    print(array_1(3, 5))
    print(array_1(4, 6))
