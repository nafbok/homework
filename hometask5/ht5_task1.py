import pickle
import string

text = "Peggy Masuku put the finishing touches on the welcome sign to her homestead in south-western Zimbabwe's Matobo district. " \
       "She surveyed her handiwork, six months of designing and painting her huts in anticipation of an annual competition, " \
       "My Beautiful Home, which recognises the most beautiful traditionally decorated homes in the district"
with open('text', 'wb') as fragment:
    pickle.dump(text, fragment)
with open('text', 'rb') as fragment:
    text1 = pickle.load(fragment)
letter = 0
for i in text1.strip():
    if i == ' ' or i == "'" or i == ',' or i == '-' or i == '.':
        continue
    else:
        letter += 1
with open('text') as fragment:
    count_lines = 0
    for line in fragment:
        count_lines += 1
print('Quantity of the letters: ', letter)
print('Quantity of the words: ', len(text.split()))
print('Quantity of the strings: ', count_lines)