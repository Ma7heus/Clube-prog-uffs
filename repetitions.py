DNA = list(input())
cont = 0
listNumber =[]
N = DNA[0]
p = 0

for i in DNA:
    if i == N:
        cont += 1
        N = i
    else:        
        cont = 1
        N = i
    listNumber.append(cont)

for i in listNumber:
    if i>p:
        p=i

print(p)
