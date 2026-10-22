n=int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    print("*", end="")
    for j in range(2*i-1):
        print(" ", end="")
    if i != 0:
        print("*", end="")

    print()

for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    print("*", end="")
    for j in range((2*n-3)-(i+1)*2):
        print(" ", end="")
    if i != n-2:
        print('*', end="")


    print()