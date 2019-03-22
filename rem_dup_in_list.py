numbers = [1, 2, 10, 3, 8, 2, 6, 8, 8, 9, 10]
print(numbers)
for items in numbers:
    count = 0
    for i in numbers:
        if items == i:
            count += 1
            if count >1:
                numbers.remove(i)

print(numbers)