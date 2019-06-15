#To find odd &Even in the list

#find ood and even in user input

def odd_even(list_ip):
    user_ip = list_ip[0]
    even=[]
    odd=[]
    for i in list_ip:
        if i % 2 == 0:
            even.append(i)          #Even numbers append in the list
        else:
            odd.append(i)           #odd numbers append in the list
            list_ip = odd + even    #merge odd and even numbers
    return list_ip

if __name__ == "__main__":
    list_ip = input("Enter the number:: ").split(" ")
    lst = []
    for i in list_ip:
        lst.append(int (i))
    list_ip = lst
    print(odd_even(list_ip))
