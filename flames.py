def matching(inp):
    str = len("FLAMES")
    while inp > str:
        if inp % str != 0:
            return str



if __name__ == "_main":
    inp = int(input("Enter the number")
    print(matching(inp))
