# This program returns commaline arugument
import sys

# This function prints user input at command line
def command(arg, arg1, arg2):
    print(arg)
    print(arg1)
    print(arg2)
    

# Main
if __name__ == "__main__":
    arg = sys.argv[0]
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(command(arg, arg1, arg2))
