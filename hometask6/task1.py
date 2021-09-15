comand = input('Enter command: ')
comand_list = ['+', '-', '%', '/', '*']
i = 0
while 1 > 0:
    if comand in comand_list:
        num1 = input('Enter first number: ')
        num2 = input('Enter second number: ')
        break
    else:
        print('You enter wrong command.')
        comand = input('Enter command: ')

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def modulo(x, y):
    return x % y

def multiplication(x, y):
    return x * y

def devision(x, y):
    if y == 0:
        return 'Error. It is forbidden to divide by zero'
    else:
        return x / y

if comand == '+':
    print('Result = ', plus(int(num1), int(num2)))
elif comand == '-':
    print('Result = ', minus(int(num1), int(num2)))
elif comand == '%':
    print('Result = ', modulo(int(num1), int(num2)))
elif comand == '*':
    print('Result = ', multiplication(int(num1), int(num2)))
elif comand == '/':
    print('Result = ', devision(int(num1), int(num2)))

