"""
Empacotamento e desempacotamento de dicionarios
"""

a, b = 1 , 2
a, b = b , a

print(a,b)

print()

pessoa = {
    'nome':'Joana',
    'sobrenome':'Souza',
}

#args e kwargs
#args -> argumentos não nomeados
#kwargs -> argumentos nomeados

a1,b1 = pessoa 
print(a1,b1)
print()

a2, b2 = pessoa.values()
print(a2,b2)
print()

a,b = pessoa.items()
print(a,b)
print()

(a1,a2),(b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)
print()


for chave, valor in pessoa.items():
    print(chave,valor)

print()
dados_pessoa = {
    'idade': 16,
    'altura':1.6,
}

print(pessoa,dados_pessoa)
print()

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print()

#usando kwargs
def mostra_argumentos_nomeados(*args,**kwargs):
    for chave, valor in kwargs.items():
        print(chave,valor)

mostra_argumentos_nomeados(nome='Joana',qlq = 123)
print()

mostra_argumentos_nomeados(**pessoa_completa)
print()

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostra_argumentos_nomeados(**configuracoes)