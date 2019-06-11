# This program greets based on time
import time, firstname

# Function return current time
def get_time():
    return time.strftime('%H')

# Greets the user based on current time
def greet_user(user_name = "Your Name"):
    if int(get_time()) < 12:
        print(firstname.firstname(user_name, "Good Morning"))
    elif int(get_time()) > 12:
        print(firstname.firstname(greeting_message = "Good Afternoon",name = user_name))
    else:
        print("Good Night")


if __name__ == "__main__":
    greet_user("Jayanth Nagaraj")
    # print(type(get_time()))
