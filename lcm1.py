# This progran to find lcm of 2 numbers
# Find lcm function
def lcm(num1, num2):
    if num1>num2:
        min = num1
    else:
        min = num2

# Always 1
    while 1:
        if min%num1 == 0 and min%num2 == 0:
            lcm = min
            break
        min = min+1
    return lcm

# Main
if __name__ == "__main__":
    num1=8
    num2=6
    print("LCM-->", lcm(num1, num2))
