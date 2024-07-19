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
pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda,'
}

#len
print(len(pessoa))

print()
#keys

print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))
for chave in pessoa.keys():
    print(chave)

print()

#values
print(pessoa.values())
print(tuple(pessoa.values()))
print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print()

print(pessoa.items())
print(tuple(pessoa.items()))
print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

print()

#setdefault

print(pessoa.setdefault('idade',None))
print(pessoa['idade'])