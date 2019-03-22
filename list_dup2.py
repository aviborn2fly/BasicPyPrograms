numbers = [2,4,3,5,7,2,9,10,6,5,10]
print(numbers)
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)