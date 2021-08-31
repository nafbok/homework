hotels = {'Continental Hotel': '****',
          'Big Street Hotel': '**',
          'Corner Hotel': '**',
          'Trashviews Hotel': '*',
          'Hazbins Hotel': '****',
          'Hazbims Delux': '*****'}
stars = input('Please enter stars: ')
for key, value in hotels.items():
    if len(value) == len(stars):
        print(key, value)