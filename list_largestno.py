def large_no(user_ip):
    max_value = user_ip[0]
    for i in user_ip:
        if i > max_value:
            max_value = i
        #lst.append(list)
    return max_value

if __name__ == "__main__":
    user_ip = input("Enter thr number::  ").split(" ")
    lst = []
    for i in user_ip:
        lst.append(int (i))
    user_ip = lst
    print(large_no(user_ip))
