h = int(input("Enter a number: "))

if h == 2:
    print(' *')
    print("***")
else:

    for i in range(h):
        
        for j in range(h-i-1):
            print(" ", end="")
            
        if i == h-1:
            for j in range(2*h-1):
                print('*', end="")
        else:
        
            print('*', end= '')
        
        for j in range(2*i-1):
            print(" ", end="")
        
        if i != 0 and i!=h-1:
            print('*', end="")
            
        print()
