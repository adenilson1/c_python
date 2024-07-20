"""
Métodos utéis para dicionarios em python

len - quantas chaves
keys - iteráveis com chaves
values - itaráveis com valores 
items - itavráveis com chaves e valores 
setdefault - adiciona valor se a chave não existe
copy - retorna uma copia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave específicamente (del)
popitem - apaga o último item adicionado
update - atualiza um dicionario com outro
"""

import copy
d1 = {
    'c1':1,
    'c2':2,
    'l1':[1,2,3],
}


d2 = d1 # não é uma copy, d2 aponta para o mesmo dicionario de d1
print(d1)
print(d2)
d2['c1'] = 1000

print()
#copy
d2 = d1.copy() # copia rasa
print(d1)
print(d2)

print()
d2['l1'][1] = 9999
print(d1)
print(d2)

print()

#usando a biblioteca
d2 = copy.copy(d1)
print(d1)
print(d2)

#copia profunda
print()
d2 = copy.deepcopy(d1)
print(d1)
print(d2)


