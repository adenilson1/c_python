#argumentos

def soma(*args):
    total = 0
    for n in args:
        total += n
    return total


soma_1_2_3 = soma(1,2,3,4,5,6)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

#empacotamento
numeros = 1,2,3,4,5,6,7,78,10

outra_soma = soma(*numeros)
print(outra_soma)

print(numeros)

#desempacotamento
print(*numeros)