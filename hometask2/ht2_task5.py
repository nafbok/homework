import random
symbols = input('Enter desired quantity symbols of the new password: ')
symbols = int(symbols)
while symbols < 8 or symbols > 16:
    print('Wrong number of symbols. Correct entry is greater than 8 and less than 16')
    symbols = input('Enter correct number of symbols: ')
    symbols = int(symbols)
numbers = '1234567890'
lower_letters = 'qwertyuioplkjhgfdsazxcvbnm'
upper_letters = lower_letters.upper()
set_symbols = numbers + lower_letters + upper_letters
set_symbols = list(set_symbols)
random.shuffle(set_symbols)
i = 0
password = list()
while i < symbols:
    password.append(random.choice(set_symbols[i]))
    i += 1
print('Your new password is: ', ''.join(password))
