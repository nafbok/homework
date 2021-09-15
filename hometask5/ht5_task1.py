import string

text = "Peggy Masuku put the finishing touches on the welcome sign to her homestead in south-western Zimbabwe's Matobo district. " \
       "She surveyed her handiwork, six months of designing and painting her huts in anticipation of an annual competition, " \
       "My Beautiful Home, which recognises the most beautiful traditionally decorated homes in the district"
with open('text', 'w') as fragment:
    fragment.write(text)
with open('text', 'r') as fragment:
    count_lines1 = fragment.readlines()
    print(count_lines1)
letter = 0
for i in text.strip():
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
