# This program converts user input as uppercase lowercase and camale case
# This function converts uppercase to lower case
def lwr_str(str):
    lower=str
    for i in range(0,len(lower)):
        if ord(lower[i]) > 64 and ord(lower[i]) <= 90: 
            lower =lower[:i] + chr(ord(lower[i]) + 32) + lower[i+1:]
    return lower

# This function converts lower case to uppercase
def upper_str(str):
    upper=str
    for i in range(0, len(upper)):
        if ord(upper[i]) > 90 and ord(upper[i]) <= 122:
            upper = upper[:i] + chr(ord(upper[i]) - 32) + upper[i+1:]
    return upper

# Main
if __name__ == "__main__":
      str=input("Enter the String:")
      print (lwr_str(str))
      print(upper_str(str))
