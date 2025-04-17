# copilot : disable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
    
if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
elif operator == '*':
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')
elif operator == '/':
         result = num1 / num2
         print(f'{num1} / {num2} = {result}')
