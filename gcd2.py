# This program for to print GCD of two number
# This function used to find GCD
def gcd(n1, n2):
    if n2 != 0:
        return gcd(n2, n1%n2)
    else:
        return n1

# Main    
if __name__ == "__main__":
    n1 = int(input("Enter the values of num A>>>"))
    n2 = int(input("Enter the value of Num B>>>"))
    print(gcd(n1, n2))
