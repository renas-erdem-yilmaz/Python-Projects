n = int(input("Type how many inputs you want to give:  "))
myList = []
distinctvaluecount = 0


for i in range(n):
    number = int(input(": "))
    myList.append(number)
    if n == 1:
        print("No second largest")
    
for i in range(len(myList)-1):
    for j in range(len(myList)-1):
        if myList[j] > myList[j+1]:
            myList[j], myList[j+1] = myList[j+1], myList[j]
            
for i in range(len(myList) - 1, 0, -1):
    if myList[i] != myList[i-1]:
        print(myList[i-1])
        distinctvaluecount += 1
        break
    else:
        continue
    
if distinctvaluecount == 0 and n != 1:
    print("No second largest")


    
    

