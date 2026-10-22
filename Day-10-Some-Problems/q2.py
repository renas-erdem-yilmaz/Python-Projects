numbers = [2, 5, 3, 8, 1]
count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1
        numbers[i] -= count
    else:
        numbers[i] += numbers[i - 1]

print(numbers)
print(count)