n = int(input())
numbers = input().split()
newn = []
numberList = []
soma1 = 0
soma2 = 0
total = 0

#tranforma a lista string em int
for i in numbers:
    newn.append(int(i))

for j in range(1,n+1):
    numberList.append(int(j))

soma1 = sum(newn)
soma2 = sum(numberList)
total = soma2 - soma1

print(total)





