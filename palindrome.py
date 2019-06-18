# This program for to check given string is palindorme or not
# This function to check palindrome
def palindrome(s):
        # Reverse the given String
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False

# Main
if __name__ =="__main__":
    s = input("String>>>")
    #print(palindrome(s))
    if palindrome(s):
        print("Palindrome")
    else:
        print("Not palindorm")
