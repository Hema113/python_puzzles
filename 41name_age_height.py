# Program for stroing data in tuples in ascending order
# package for sorting the data useing key values
from operator import itemgetter

database_info = []
while True:
    user_ip = input("Enter name,age,height>>>:")
    if user_ip == "stop" or user_ip == "STOP": # If user is input is balank and press the ENTER exit from the loop
        break
    else:
        # Split the user input and stored in tuples
        database_info.append(tuple((user_ip.split(" "))))

# Sorting the user data using itemgetter key
database_info.sort(key = itemgetter(0, 1, 2))
print("Ascending sorted tuple>>>",database_info)







"""from operator import itemgetter
def tup():
    database_info = []
    while True:
        user_ip = input("Enter name,age,height")
        if user_ip == "":
            break
        else:
            database_info.append(tuple((user_ip.split(","))))
    return database_info.sort(key = itemgetter(0, 1, 2))


if __name__ =="__main":
    print("Ascending order tuples>>>>",tup())"""
