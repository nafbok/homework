import random
symbols = input('Enter desired quantity symbols of the new password: ')
symbols = int(symbols)
while symbols < 8 or symbols > 16:
    print('Wrong number of symbols. Correct entry is greater than 8 and less than 16')
    symbols = input('Enter correct number of symbols: ')
    symbols = int(symbols)
numbers = '1234567890'
numbers_list = list(numbers)
random.shuffle(numbers_list)
lower_letters = 'qwertyuioplkjhgfdsazxcvbnm'
lower_letters_list = list(lower_letters)
random.shuffle(lower_letters_list)
upper_letters = lower_letters.upper()
upper_letters_list = list(upper_letters)
random.shuffle(upper_letters_list)
i = 0
password = list()
while i < symbols:
    while i < 2:
        password.append(random.choice(numbers_list[i]))
        i += 1
    while i < 4:
        password.append(random.choice(upper_letters_list[i]))
        i += 1
    password.append(random.choice(lower_letters_list[i]))
    i += 1
random.shuffle(password)
print('Your new password is: ', ''.join(password))

