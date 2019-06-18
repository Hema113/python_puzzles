#Print Next prime Number
# Import prime_no function from prime.py
from prime import prime_no
def next_prime(num):
    if num == 0 or num == 1:
        num = 1
    for i in range(num+1, (num*2)+1):
        if prime_no(i): # Check given num is prime or not
            num = i
            return num

# Main
if __name__ == "__main__":
    num = int(input("Enter the number"))
    print ("The next prime number is", next_prime(num))
