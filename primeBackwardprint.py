def prime_no(num):
      if (num%2)==0:
          print(num-3,"is a not prime number")
      else:
          return print(num-3," is a prime number")
if __name__ == "__main__":
    num=int(input("Enter the number check its prime or not:"))
    prime_no(num)
