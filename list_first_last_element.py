# This program prints first & last element in the given list
def list_element(ls):
    le=len(ls)
    # Retrun 1st & last index in the list
    return [ls[0], ls[le-1]]

# Main
if __name__ == "__main__":
    ls = [1, 2, 3, 6]
    print(list_element(ls))
