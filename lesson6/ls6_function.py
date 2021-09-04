import math
def max_min_list(*x):
    return max(x), min(x)
    sorted_list = sorted(x)
print(max_min_list(1,2,9,4,5))

def sort_list_or_not (*y):
    sorted_list = sorted(y)
    if tuple(sorted_list) == y:
        print(True)
    else:
        print(False)
sort_list_or_not(1,8,2)

def factorial(y):
    return math.factorial(y)
print(factorial(0))

def bus_train(ticket_price, monthly_price):
    return monthly_price//ticket_price
print(bus_train(8, 500))

def letter_in_string(letter, my_string):
    count = 0
    for i in my_string:
        if i == letter:
            count += 1
    if count == 0:
        return 'No letters'
    return count

print(letter_in_string('o', 'tratata'))

import os
inputFile = 'config.txt'
optionInput = input('Enter option: ')
with open(inputFile, mode='r+', encoding='UTF 8') as file:
    content = file.read()
    for line in file:
        if optionInput in line:
            temp_line = line.strip() # full old line
            input_value = input('Enter value: ')
            sub_temp_line = temp_line[len(optionInput)+1:]
            editLine = temp_line.replace(sub_temp_line, input_value) #full new line
with open(inputFile, mode='a+', encoding='UTF 8') as file:
