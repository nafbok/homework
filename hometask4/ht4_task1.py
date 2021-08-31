my_list = [3, 6, 5, 0, 1]
#my_list = list(range(6))
sort_my_list = my_list
sort_my_list = sorted(sort_my_list)
if my_list == sort_my_list:
    print('True: ', my_list, 'equal to', sort_my_list)
else:
    print('False: ', my_list, 'not equal to', sort_my_list)