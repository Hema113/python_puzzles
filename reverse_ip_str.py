# This Program reverse the user given sentence

def reverse(ip):
    rev = ip.split()
    r=rev[::-1]
    return r

# Main
if __name__ == "__main__":
    ip = str(input("Enter the Sentence>>>"))
    print(reverse(ip))
