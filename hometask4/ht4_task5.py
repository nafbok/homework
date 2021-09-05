hotels = {'Continental Hotel': '****',
          'Big Street Hotel': '**',
          'Corner Hotel': '**',
          'Trashviews Hotel': '*',
          'Hazbins Hotel': '***',
          'Hazbims Delux': '*****'}
stars = input('Please enter stars: ')
if stars.isdigit():
    i = int(stars)
    while i < 1 or i > 6:
        print('Wrong stars number.')
        stars = input('Enter form 1 to 5 range: ')
        i = int(stars)
    for key, value in hotels.items():
        i_value = len(value)
        if i == i_value:
            print(key, value)
else:
    while len(stars) < 1 or len(stars) > 6:
        print('Wrong stars number.')
        stars = input('Enter form 1 to 5 range: ')
    for key, value in hotels.items():
        if len(stars) == len(value):
            print(key, value)
