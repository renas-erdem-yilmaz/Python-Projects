n = int(input())
myList = []
streak = 1
longeststreak = 1
start = 0

for i in range(n):
    number = int(input())
    myList.append(number)

for i in range(len(myList) - 1):
    if myList[i + 1] > myList[i]:
        streak += 1

        if streak > longeststreak:
            longeststreak = streak
            start = i + 2 - streak
    else:
        streak = 1

runlist = myList[start:start + longeststreak]

print("Length:", longeststreak)
print("Start:", start)
print("Run:", runlist)
