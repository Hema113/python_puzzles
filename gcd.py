# Find GCD of two numbwrs
def gcd(n1, n2):

    #usewhile loop find gcd
    while(n2!=0):
        temp = n2
        n2 = n1%n2
        n1 = temp
    return n1
if __name__ == "__main__":
    n1 = int(input("Enter the values of num A>>>"))
    n2 = int(input("Enter the value of Num B>>>"))
    print(gcd(n1, n2))
