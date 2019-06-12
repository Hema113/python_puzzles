#This program is print length of given String

#Find length of given String

def console_print(str):
    count=0
    for i in str:
        count=count+1
    return count

if __name__ == "__main__":
    str=input("Enter the string")
    print(console_print(str))
