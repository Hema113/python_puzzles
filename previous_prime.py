# This function print previous prime Number
# Import prime_no function from prime.py file
from prime import prime_no
def pre_prime(num):
    for i in range(num-1, num//2, -1):
        # print(i)
        if prime_no(i): # Check prime or not
            num = i
            return num

# Main
if __name__ == "__main__":
    num=int(input("Enter the number:"))
    print("previous_prime-->",pre_prime(num))
