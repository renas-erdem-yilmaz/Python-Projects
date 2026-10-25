count = 0
passed = 0
total = 0

while True:
    score = int(input("Enter your score: "))
    
    if score == -1:
        break
    
    if 0<=score<=100:
        total += score
        count += 1
    else:
        passed += 1
    
print("Count:", count)
print("Average:", round(total/(count), 2))
print("Passed:", passed)
