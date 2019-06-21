# Prgram for Eliminate duplicate elements in list usein set

def eliminate(data):
    result =set(data) #---> Convert list to set
    return result

# Main
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 5, 5 ,6 ,7 ,8 ,9 ,9,10]
    print("Before",data)
    print("After useing set",eliminate(data))
