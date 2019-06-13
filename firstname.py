# this program extracts firstname

def firstname(name = "<First Name>", greeting_message = "Hi"):
    return greeting_message + " " + str(name.split(" ")[0])

# name=input("Enter u r first & last Name > ")
# print(firstname(name))
