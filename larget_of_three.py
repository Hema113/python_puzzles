# This program print largest of 3 variable
# Find largest number function
def large(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

# Main
if __name__ == "__main__":
    a = [90]
    b = [30]
    c = [21]
    print("large_num-->>",large(a, b, c))
