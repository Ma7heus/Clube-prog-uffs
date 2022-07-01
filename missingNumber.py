n = int(input())
numbers = input().split()
newn = []
numberList = []
total = 0
 
#tranforma a lista string em int
for i in numbers:
    newn.append(int(i))
 
for j in range(1,n+1):
    numberList.append(int(j))

total = sum(numberList) - sum(newn)
 
print(total)





