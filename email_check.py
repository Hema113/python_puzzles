# This program will check given mail_id is vaild or not
# Import regular expression package
import re
# Function for valid user input
def email_Validation(user_ip):
    # Checking mail pattern
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',user_ip):
        return True
    else:
        return False

# Main
if __name__ == "__main__":
    user_ip = input("Enter Email id:")
    if email_Validation(user_ip):
        print("Given mail_id is valid")
    else:
        print("Given mail_id is not valid")
