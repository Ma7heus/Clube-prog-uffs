numteste = int(input())
for i in range(numteste):
    x, y = map(int, input().split())
    if x==1 and y==2:
        resultado = 2
    else:
        if x >= y:
            if x % 2 == 0:
                x1 = x*x
                resultado = x1 - (y-1)
            else:
                x1 = (x-1)*(x-1) + 1
                resultado = x1 + (y-1)
        else:
            if y % 2 == 0:
                y1 = (y-1)*(y-1) + 1
                resultado = y1 + (x-1)
            else:
                y1 = y*y
                resultado = y1 - (x-1)
    print(resultado)