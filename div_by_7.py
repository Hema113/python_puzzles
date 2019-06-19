def div_7(ip1, ip2):
    res = []
    for i in range(ip1, ip2):
        if(i % 7 == 0) and (i % 5 != 0):
            res.append(str(i))
    return (','.join(res))


# Main
if __name__ =="__main__":
    ip1 = 2000
    ip2 = 3200
    print(div_7(ip1, ip2))
