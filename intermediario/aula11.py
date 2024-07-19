"""
Maniopulação de chaves e valores em dicionarios em python

Criação de um CRUD - CREATE, UPDATE E DELETE
"""

#CREATE

pessoa = {} # => dicionario

#pessoa['nome'] = 'ABCD' # -> criando a chave 'nome
#print(pessoa)

#chave dinamica

chave = 'nome'
pessoa[chave] = 'Pedro Brasil'
print(pessoa[chave])
#print(pessoa)

#UPDATE: alterar valor da chave

pessoa[chave] = 'Ana'
pessoa['sobrenome'] = 'Souza'
print(pessoa[chave])
print(pessoa)

#DELETE: apagando chave

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#trabalhando com excercões: usa-se o get

#print(pessoa.get('sobrenome', 'Não existe'))

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
