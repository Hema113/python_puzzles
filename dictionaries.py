# Program return date of birth based on name useing dictionaries

# Function for dictionaries
def dictionary(name):
    datas = {
            "Hema"    : "30-04-1995",
            "Balaji"  : "24-11-1964",
            "Aswini"  : "29-09-1996",
            "Krithik" : "25-08-2002"
            }
    return datas[name]

# Main
if __name__ == "__main__":
    name = input("Enter the name>>>")
    print(dictionary(name))
