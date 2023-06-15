numbers = [2, 3, 7, 2, 9, 3, 6, 3, 2, 6, 6, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)
