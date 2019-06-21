# Prgram for Eliminate duplicate elements in list usein set

def eliminate(data):
    result1 = []
    result =set(data) #---> Convert list to set
    result1 =list(result)
    return result1

# Main
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 5, 5 ,6 ,7 ,8 ,9 ,9,10]
    print("Before",data)
    print("After using set",eliminate(data))
