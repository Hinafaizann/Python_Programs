##Building Calculatorrrr

num1 = float(input("Enter a number: "))
op = input("Enter an operator: ") # we have to input number otherwise its going to have eroor
num2 = float(input("Enter a second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid number")

