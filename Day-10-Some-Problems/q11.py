n = int(input("Enter an integer: "))
preserver = n
length = len(str(n))
even_sum = 0
reverse = 0

for i in range(length-1, -1, -1):
    divisor = 10 ** i
    digit = preserver // divisor
    print(digit)
    
    if digit % 2 == 0:
        even_sum += digit
    
    reverse += digit * (10**(length-i-1))
    
    preserver = preserver - (digit * divisor)
    
print("Digits:", length)
print("Even sum:", even_sum)
print(reverse)

    
