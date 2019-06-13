#check wheather given num is prime or not

def prime_no(num):
    if num == 2:
        return True
    elif num%2 == 0 and num > 2:
        return False
    else:
        for i in range(3, int(num/2), 2):
            print(i)
            if (num % i) == 0:
                return False
        return True

        
def main():
    num=int(input("To check given its prime or not:"))
    if prime_no(num):
        print("Given number is  prime number", num)
    else:
        print("Given Number is not prime number", num)

if __name__ == "__main__":
    main()
    #Getting input from user
