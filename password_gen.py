import random

def main():
    pass_len= int(input("Enter the password length"))
    print("your password is>>>>",password(pass_len))

def password(pass_len):
    str="abcdefghijklmnopqrstuvwxyz0123456789ABCEFGHIJKLMNOPQRSTUVWXYZ!@#%"
    password = "".join(random.sample(str, pass_len))
    return password

if __name__ == "__main__":
    main()
