number = int(input("Enter a number: "))

times = len(str(number))
x=0
for i in range(times):
    x = number // (10**(times-1)) - x*(10**(times-2))
    print(x)
