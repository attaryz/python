# remove duplicates in the first list
# and add them to the second list
numbers = [2, 8, 2, 7, 3, 8, 9, 1, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)