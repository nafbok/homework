# my_file = open('my_file', 'w')
# my_file.write('Anna Bokareva')
# my_file.close()
# lorem_file = open('Lorenm', 'w')
# lorem_file.write('Lorem')
# lorem_file.close()
# lorem_file = open('Lorenm', 'r')
# print(lorem_file.readlines())
import pickle
student_marks = open('student marks', 'w')
data = {'Avramenko':3, 'Avratynsky': 4, 'Babich': 2}
student_marks.close()
pickle.dump(data, open('student marks', 'wb'))
student_marks2 = pickle.load(open('student marks', 'rb'))
for key, value in student_marks2.items():
    if value > 3:
        print(key, value)
summa = 0
for value in student_marks2.value():
    summa += value / len(value)
    print(summa)
#print(student_marks2)






