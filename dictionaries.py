# Program return date of birth based on name useing dictionaries

# Function for dictionaries
def dictionary(birthday_data,name):
    temp = []
    for data in birthday_data["birthday"]:
        if ["Name"] == name:
            temp.append((data["DOB"], data["ID"])
        else:
            break
    return temp


# Main
if __name__ == "__main__":
    birthday_data = {
            "birthday":
            [
            {
            "ID": 1,
            "Name": "Hemachandran",
            "DOB": "30-06-1995"
            },
            {
            "ID": 2,
            "Name": "Hemachandran",
            "DOB": "30-04-1996"
            }
            {
            "ID": 30,
            "Name": "Balaji",
            "DOB": "24-011-1964"
            }
            ]
            }

    name = input("Enter the name>>>")
    result = dictionary(birthday_data,name)

    if result == []:
        print("Data not found")

     else:
         for i in result:
             print(name,"DOB>>>",i[0],"ID>>>",i[1])
