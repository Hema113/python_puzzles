arr =[[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

row=5
col=5
for i in range(col):
    if (i%2==0):
        for j in range(col-1,-1,-1):
            print(arr[j][i], end=" ")
        #print(",")
    else:
        for j in range(row):
            print(arr[j][i], end = " ")
        #print(",")
