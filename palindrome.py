def palin(str):
    l_indx=0
    h_indx =len(str)-1
    while(h_indx > l_index):
        if (str[l_indx++]) != (str[h_indx--])):
            return False
        else:
            return True
        return str
if __name__ == "__main":
    str = input("String")
    if palin(str):
        print("palindorm", str)
    else:
        print("Not palindorm", str)
