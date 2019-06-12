#check wheather given num is prime or not

def prime_no(num):

    #given number is greater than 1

    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
                break
            else:
                return True

if __name__ == "__main__":
    #Getting input from user

    num=int(input("To check given its prime or not:"))
    if prime_no(num):
        print("Given number is not prime number", num)
    else:
        print("Given Number is prime number", num)
