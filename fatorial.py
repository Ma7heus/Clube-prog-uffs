#fatoria usando funcao recursiva

def fatorial(n):
    if n == 0 or n ==1:
        return 1

    return fatorial(n -1)*n
    

print(fatorial(4))


