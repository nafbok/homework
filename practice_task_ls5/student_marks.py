import pickle

#data
data = {'Avramenko': 3,
        'Avratinsky': 4,
        'Ivanov': 5,
        'Petrova': 2,
        'Suharev': 3,
        'Sidorov': 5}

#dump in the file
with open('student_marks', 'wb') as student:
    pickle.dump(data, student)

#load data from file
with open('student_marks', 'rb') as student:
    studentslist = pickle.load(student)

#output students with marks less 4
markslist = list(dict.values(studentslist))
markslistlessfour = []
for i in markslist:
    if i < 4:
        markslistlessfour.append(i)
    else:
        continue
print('Student list  with marks less 4: ')
for key, value in studentslist.items():
    if value in markslistlessfour:
        print(key, value)

#average marks
allmarks = 0
average_mark = 0
for i in markslist:
    allmarks += i
average_mark = allmarks/len(markslist)
print('Average marks is\n', round(average_mark, 2))

#excellent students
print('Excellent student list: ')
for key, value in studentslist.items():
    if value == 5:
        print(key, value)

#new file and load dictionary there
with open('new student list', 'wb') as new_list:
    pickle.dump(studentslist, new_list)

#load data and asc list
with open('new student list', 'rb') as new_list:
    new_student_list = pickle.load(new_list)
print('Sorted student list by marks')
sorted_values = sorted(new_student_list.values())
sorted_list = {}
for i in sorted_values:
    for k in new_student_list.keys():
        if new_student_list[k] == i:
            sorted_list[k] = new_student_list[k]
for key, value in sorted_list.items():
    print(key, ' - ',  value)








