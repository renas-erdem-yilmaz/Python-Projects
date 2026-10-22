mid=0
leftpart = 0
rightpart = 0
myList = [15, 1, 2, 4,7,2]

while True:
    for i in range(len(myList)):
        if i < mid:
            leftpart += myList[i]
        elif i > mid:
            rightpart += myList[i]

    if leftpart == rightpart:
        print(f"The number {myList[mid]} is the midpoint the index is {mid}")
        break
    else:
        mid += 1
        leftpart = 0
        rightpart = 0
        if mid > len(myList):
            print("There is no mid point")
            break