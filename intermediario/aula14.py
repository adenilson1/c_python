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
p1 = {
    'nome': 'Luiz',
    'sobrenome':'Miranda',
}

print(p1.get('nome','nao existe'))
print(p1)
print()

#pop
nome = p1.pop('nome')
print(nome)
print(p1)
print()

#item
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
print()

#update
p1.update({
    'nome':'novo valor',
    'idade':30,
})
print(p1)
print()

p1.update(nome='novo valor', idade=30, soborenome='Miranda')
print(p1)
print()

tupla =(('nome','novo valor'),('idade',35))
p1.update(tupla)
print(p1)
print()

lista = [['nome','novo valor'],['idade',40]]
p1.update(lista)
print(p1)

