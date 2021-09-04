numbers = input('Enter the numbers set: ')
num_list = list()
for item in numbers.split():
    if item.isdigit():
        num_list.append(item)
result = 0
for item in num_list:
    result += int(item)
print('Sum = ', result)

