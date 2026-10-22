numbers = [2, 3, -1, 5, 6, 7, -2, 8]

longest = 0
current = 0

for i in range(len(numbers)):
    if i != 0:
        if numbers[i] > numbers[i-1]:
            current += 1
        else:
            current = 0

    longest = max(current, longest)

print("Longest streak:", longest)