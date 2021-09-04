user_input = input("Enter numbers: ")
set_numbers = list(user_input)
set_numbers_sort = sorted(set_numbers)
if set_numbers == set_numbers_sort:
    print('True: ', set_numbers, 'equal to', sorted(set_numbers_sort))
else:
    print('False: ', set_numbers, 'not equal to', sorted(set_numbers_sort))