import math
#<-------------------Basic Opearations---------->
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

# factorial
def factorial(num1):
    fact = 1
    for i in range(1,num1+1):
        fact *= i
    return fact

# Prime or not
def prime_1(num1):
    if num1 == 2:
        return "Prime"
    elif num1%2 == 0 and num1 > 2:
        return "Not Prime"
    else:
        for i in range(3, int(num1/2), 2):
            print(i)
            if (num1 % i) == 0:
                return "Not prime"
        return "Prime"

# <-------------------- Scientific Calculations -------------------->
def sin_op(num1):
    return ("sin",(num1), "=", math.sin(num1 ))

def cos_op(num1):
    return ("cos",num1,"=", math.cos(num1))

def tan_op(num1):
    return ('tan',num1,'=', math.tan(num1))

def pie_op(num1):
    return ('Pie',num1,'=', math.pi)

def log_op(num1):
    return ('log', num1 ,'=', math.log(num1))

print("Select your choice")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.odd_even")
print("6.factorial")
print("7.Prime")
print("8.Sin")
print("9.cos")
print("10.tan")
print("11.PI")
print("12.log")

choice = input("Enter your choice(1/2/3/4/5/6/7/8/9/10/11/12):")
#num = int(input("Enter number>>"))
num1 = int(input("Enter num>>"))
num2 = int(input("Enter num>>"))

# User selcted operation will be done
if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, mun2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
elif choice == '5':
    print(odd_even(num1))
elif choice == '6':
    print(factorial(num1))
elif choice == '7':
    print(prime_1(num1))
elif choice == '8':
    print(sin_op(num1))
elif choice == '9':
    print(cos_op(num1))
elif choice == '10':
    print(tan_op(num1))
elif choice == '11':
    print(pie_op(num1))
elif choice =='12':
    print(log_op(num1))
else:
    print("invaild input")
# #elif op == "sin":
#     print ("sin(", secondNumber, ")=", math.sin(secondNumber ))
# elif op == "cos":
#     print ("cos(", secondNumber, ")=", math.cos
#     (secondNumber ))
# elif op == "tan":
#     print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
# elif op == "pie" or op == "pi":
#     print ("Pie =", math.pi)
# elif op == "e":
#     print = ("E =", math.e)
# elif op == "ln":
#     print ("ln(", secondNumber , ")= ", math.log(secondNumber))
# else:
#     print ("incorrect operator")
