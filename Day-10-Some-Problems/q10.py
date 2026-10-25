n = int(input("Enter your integer: "))
constant = n
myList = []

if n == 0:
    print("Binary: 0")
    print("Ones: 0")
else:
    while constant != 0:
        remainder = constant % 2
        constant = constant // 2
        myList.append(remainder)
        
print("Binary:", end=" ")
for element in myList[::-1]:
    print(element, end="")

print("\nOnes:", myList.count(1))

        
