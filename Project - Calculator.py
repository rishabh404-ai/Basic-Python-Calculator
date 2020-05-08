def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('You can perform the following operation :\n'
      '1. Addition\n'
      '2. Subtraction\n'
      '3. Multiplication\n'
      '4. Division')

choice = input('Enter the choice of operation(1/2/3/4) :')
num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number: '))
if choice == '1':
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == '4':
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Invalid Input')
