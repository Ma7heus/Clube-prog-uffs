# Funcao que resolve a potencia de dois numeros
def potenciacao(base,expoente):
    return(base**expoente)

print(potenciacao(int(input()),int(input())))
#nesse caso estou usando o input fora da função,
#mas posso fazer dentro dela, e deixala sem parametros na chamada.