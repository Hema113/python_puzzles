def fibo(user_inp):
    t1 = 0
    t2 = 1
    a = [t1, t2]
    for i in range(0,user_inp-1):
        temp = t1 + t2
        t1 = t2
        t2 = temp
        a.append(temp)
    return a

if __name__ == "__main__":
    user_inp = int(input("Enter the number"))
    print(fibo(user_inp))
