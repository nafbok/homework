dictionary = {'salt': 2,
              'meat': 25,
              'apples': 6,
              'banana': 3,
              'milk': 4.5,
              'bread': 2.5}
values_list = list((dict.values(dictionary)))
values_list = sorted(values_list)
slice_values_list = values_list[-3:]
for key, value in dictionary.items():
    if value in slice_values_list:
        print(key, value)
