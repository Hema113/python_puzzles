# This program print largest of 3 variable
# Find largest number function
def large(a, b, c):
    if a > b:
        return a
    elif b > c:
        return b
    else:
        return c

# Main
if __name__ == "__main__":
    a = [21]
    b = [16]
    c = [12]
    print("large_num-->>",large(a, b, c))
