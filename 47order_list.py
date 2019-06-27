def sort_ing(ip_list):
    for i in range(len(ip_list)):
        for j in range(i+1, len(ip_list)):
            if ip_list[i] > ip_list[j]:
                ip_list[i], ip_list[j] = ip_list[j], ip_list[i]
    return ip_list

if __name__ == "__main__":
    ip_list = [-5, 10, 50, 5, 2 ,1 ,100, 80 , 60, 35]
    search = int(input("Enter number u want be Search>>"))
    print("Before>>",ip_list)
    result=sort_ing(ip_list)
    print("Ascending order>>>",result)
    if search in result:
        print(search,"is available in list")
    else:
        print(search,"Not available")
