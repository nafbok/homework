# x = lambda str1: str1.upper()
# print(x('aaa'))
#
# print((lambda str2: str2.upper())('hello'))
#
#values = [1, 2, 3, 4, 5]
# def inc(value):
#     return value + 10
# print(list(map(inc, values)))
# values = ['hello', 'anna']
# def my_map(arg1):
#     return arg1 + '!'
# print(list(map(my_map, values )))
# values = [3, 6, 9]
# print(list(map(lambda i: i * 3, values)))

#print((lambda list1: ''.join(list1))(['qw', 'er']))

#****************фильтр*************
#print(list(filter((lambda x: x>0, range(-5, 5)))

#print(list(filter((lambda x: x.isupper()), 'HeLLo')))

# def my_filter(func, args):
#     result = []
#     for i in args:
#         if func(i):
#             result.append(i)
#     return result
# print(my_filter(lambda x: x.isupper(), 'HeLLo'))

#*******************reduce**************
# from functools import reduce
# product = reduce((lambda x, y: x + y), '123', '456')
# print(product)

#******************sorted_lambdda*****

# subjects = [('English', 88), ('Science', 90), ('Social science', 82)]
# subject_marks.sort(key=lambda x: x[1], reverse = True)
# print(subject_marks)
#
# models = [{'make': 'Nokia', 'model':216, 'color': 'Black'}, {'make': 'Samsung', 'model': 32, 'color': 'White'}]
# sorted_models = sorted(models, key = lambda x: x['model'])
# print(sorted_models)

#********************comprehensios***************

old_list = [1, 2, 7, 10]
my_list = [el for el in old_list if el % 2 == 0]
print(my_list)

res = []
for x in old_list:
    if x % 2 == 0:
        res.append(x)
print(res)

dictionary = {1:2, 3:4}
dict_comp = {key:value for (key, value) in dictionary.items() if key == 1}
print(dict_comp)

dictionary = {'key': 'value'}
dictionary_comp1 = {key: value for value, key in dictionary.items()}
print(dictionary_comp1)

