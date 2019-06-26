def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def odd_even(num1):
    if num % 2 == 0:
        return ("Even>>>",num)
    else:
        return ("odd>>>", num)

print("Select your choice")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.odd_even")

choice = input("Enter your choice(1/2/3/4/5):")
#num = int(input("Enter number>>"))
num1 = int(input("Enter num>>"))
num2 = int(input("Enter num>>"))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, mun2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
elif choice == '5':
    print(odd_even(num))
else:
    print("invaild input")
