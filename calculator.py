num1 = float(input("enter number1 "))
operator = input("enter operator: ")
num2 = float(input("enter number2 "))
def calc():
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "^":
        print(num1**num2)
    else:
        print("please put operator")
calc()