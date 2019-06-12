#Print Next prime Number
#main Function

def main():
    num = int(input("Enter the number"))
    print ("The next prime number is", next_prime(num+1))

def next_prime(num):
    return prime_no(num, num*2)

#This function checks wheather given number is prime or  not
def prime_no(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if (p % i) == 0:
                #return False
                break
            else:
                return p
            return None

if __name__ == "__main__":
    main()
