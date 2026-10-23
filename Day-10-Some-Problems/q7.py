n = int(input(": "))

for i in range(n):
    for j in range(n-i):
        print(" ", end="")

    if i == 0:
        print(1, end="")
    else:
        for j in range(2*i+1):
            if j<=(2*i+1)//2:
                print(j+1, end="")
            else:
                print(2*i+1-j, end="")

    print()