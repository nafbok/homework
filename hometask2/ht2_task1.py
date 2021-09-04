custom_str = input('Enter the string: ')
vowel_counter = 0
for i in custom_str.lower():
    if i == 'a' or i == 'e' or i == 'u' or i == 'y' or i == 'i' or i == 'o':
        vowel_counter += 1
print(vowel_counter, 'vowels')


