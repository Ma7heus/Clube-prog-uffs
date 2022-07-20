n = int(input())
listaimpar = []
listapar = []
lista = []
if n <= 3 and n != 1:
  print('NO SOLUTION')
else:
  for i in range(2, n+1, 2):
    listapar.append(i)
  for i in range(1, n+1, 2):
    listaimpar.append(i)
  lista = listapar + listaimpar
  print(*lista)
