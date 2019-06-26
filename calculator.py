def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("Select your choice")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice = input("Enter your choice(1/2/3/4):")

num1 = int(input("Enter num1>>"))
num2 = int(input("Enter num2>>"))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, mun2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
else:
    print("invaild input")
