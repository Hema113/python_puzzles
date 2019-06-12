
def lwr_str(str):
    lower=str

    for i in range(len(lower)):
        if ord(lower[i]) >=64 and ord(lower[i])<=96:
            lower = ord(chr(lower[i] + 32)
        return lower

if __name__ == "__main__":
      str=input("Enter the String:")
      print (lwr_str(str))
