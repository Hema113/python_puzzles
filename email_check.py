import re

def email_Validation(user_ip):
    if re.match(^(([A-Za-z0-9]+_+)|([A-Za-z0-9]).com, user_ip):
        return True
    else:
        return False

if __name__ == "__main__":
    userip = input("Enter Email id:")
    if email_Validation(user_ip):
        print("Given mailid is valid")
    else:
        print("Given mailid is not valid")
