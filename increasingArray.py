nvalores = int(input())
lista = list(map(int, input().split()))
cont = 0
 
for i in range(nvalores):
  if i == 0:
    continue
  if lista[i] < lista[i-1]:
    r = lista[i-1] - lista[i]
    lista[i] = lista[i] + r
    cont += r
print(cont)