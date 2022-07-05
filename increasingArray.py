def potenciacao(base,expoente):
    a = potenciacao(base**expoente)
    b = potenciacao(2**5)
    return(a+b)
    


print(potenciacao(2,4))
