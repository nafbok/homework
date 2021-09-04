import os
os.path.exists('C:\\Windows')
with open('student_marks') as student:
    line = student.readlines()
print(len(line))