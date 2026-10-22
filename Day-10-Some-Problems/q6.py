numbers = [1, 2, 3, 4]
k = 6

n = len(numbers)

if n == 0:
    rotated_list = []
else:
    effective_k = k % n
    
    split_index = n - effective_k
    
    rotated_list = []
    
    for i in range(split_index, n):
        rotated_list.append(numbers[i])
        
    # 2. Append the elements from the beginning
    for i in range(split_index):
        rotated_list.append(numbers[i])

print(rotated_list)