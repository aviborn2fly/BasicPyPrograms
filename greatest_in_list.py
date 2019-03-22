nums = [1, 200, 4, 6, 10, 20]
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i

print(largest)