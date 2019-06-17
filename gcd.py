def gcd(a, b):
    while(a != 0):
        temp = b
        a % b == 0
        temp = a
    return a
if __name__ == "__main__":
    a = int(input("Enter the values of num A>>>"))
    b = int(input("Enter the value of Num B>>>"))
    print(gcd(a, b))
