arr =[[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
row =5
col =5
#if row==col:
for i in range(row):
    for j in range(col):
        if (i==j or j==(col-1-i)):
            print(arr[i][j], end=" ")
        else:
            print(" ", end=" ")
    print(" ")
