#potenciacao usando funcao recursiva
def potenciaDe2(n):
    if n ==0:
        return 1

    return potenciaDe2(n-1)*2

print(potenciaDe2(5))