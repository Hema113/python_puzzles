def prime_no(num):
      if (num%2)==0:
          print(num,"is a not prime number")
      else:
           print(num," is a prime number")
if __name__ == "__main__":
    num=int(input("To check given its prime or not:"))
    prime_no(num)
