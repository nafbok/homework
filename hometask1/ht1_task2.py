num1 = input('What is the first number? ')
num2 = input('What is the second number? ')
if num1.isdigit() > 0 and num2.isdigit() > 0:
    digit1 = int(num1)
    digit2 = int(num2)
    print('1. The sum is = ', digit1 + digit2)
    print('2. Number 1 minus number 2 = ', digit1 - digit2)
    print('3. Power = ', digit1 ** digit2)
    if digit2 == 0:
        print('4. Error. Cannot be divided by zero')
    else:
        print('4. 1st number divides 2d = ', digit1 / digit2)
else:
    print('You entered either a negative number or not a number')
