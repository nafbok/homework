numbers = list(map(int, input('Enter the numbers set: ').split()))
summa = 0
for i in numbers:
    if i % 2 == 0 and i > 0:
        summa += i
print(summa)
