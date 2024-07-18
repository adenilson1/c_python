"""
Dicionario em python(tipo dict)
Dicionario são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como o "indice" que vimos na lista e podem
ser de tipos imutaveis como: str,int,float,tuple, etc.
O valor pode ser de qualquer tipo, incuindo outro dicionario.
Usamos as chave --{}-- ou a classe dict para cirar diconarios.
Imutavies: str, int,float,bool,tuple
mutaveis: dict, list
"""

pessoa = {
    'nome':'Adenilson Lima',
    'sobrenome':'Diniz',
    'idade': 41,
    'altura':1.8,
    'endereco': [
        {'rua':'tal tal','numero':123},
        {'rua':'outra','numero':321},
    ],
}

print(pessoa, type(pessoa))

print(40*'-')

print(pessoa['nome'])
print(pessoa['sobrenome'])

print(40*'-')

for chave in pessoa:
    print(chave,pessoa[chave])

