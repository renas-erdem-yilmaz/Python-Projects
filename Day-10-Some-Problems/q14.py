n = int(input("Type how many inputs you want to give:  "))
numbers = []
count = 0
uniquenumbers = []

for i in range(n):
    number = int(input(": "))
    if number not in numbers:
        uniquenumbers.append(number)
    numbers.append(number)

for number in uniquenumbers:
    for val in numbers:
        if number == val:
            count += 1
    print(number, count)
    count = 0
    
    
    
    
    
