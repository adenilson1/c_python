"""
Funções lambda em python

A função lambda é uma função como qualquer outra em python.
Porém, são funções anônimas que contém apenas uma linha.
OU seja, tudo deve ser contido dentro de uma única expressão.
"""

lista = [
    {'nome':'Luiz','sobrenome':'Miranda'},
    {'nome':'Marcia','sobrenome':'Oliveira'},
    {'nome':'Daniel','sobrenome':'Silva'},
    {'nome':'Eduardo','sobrenome':'Moreira'},
    {'nome':'Aline','sobrenome':'Sousa'},
]

#ordenando a lista
lista1 = [4,32,1,34,5,6,6,21]
lista1.sort()
print(lista1)
print()

#usando uma funçã
def ordena(item):
    return item['sobrenome']

lista.sort(key=ordena)

for item in lista:
    print(item)
    print()

print()

#usando lambda
lista.sort(key=lambda item:item['nome'])
for item in lista:
    print(item)

print()
print(40*'-')
#usando lambda com copias rasas
def exibe(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item:item['nome'])
l2 = sorted(lista, key=lambda item:item['sobrenome'])

exibe(l1)
exibe(l2)