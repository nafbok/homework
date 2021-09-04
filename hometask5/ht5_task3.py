inputFile = 'config.txt'
with open(inputFile, mode='r', encoding='UTF 8') as file:
    content = file.readlines()
optionInput = input('Enter option: ')
for num, line in enumerate(content):
    if optionInput in line:
        print(content[num].strip())
        input_value = input('Enter value: ')
        content[num] = line[:len(optionInput)] + ' ' + input_value + ';\n'
        print(content[num].strip())
print(content)
with open(inputFile, mode='w') as file:
    file.write(''.join(content))














