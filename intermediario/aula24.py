"""
Mapeamento de dados em list comprehension (map)
usando em lista com o mesmo tamanho
"""
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print()

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
print()

#mapeamento
produtos = [
    {'nome':'p1','preço':20,},
    {'nome':'p2','preço':10,},
    {'nome':'p3','preço':30,},
]

novos_produtos = [ 
    produto 
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()
novos_produtos = [
    produto['nome']
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()
novos_produtos = [
    produto['preço']
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()
#outra forma

novos_produtos = [
    {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()
#mudando preços com mapeamento
novos_produtos = [
    {**produto, 'preço':produto['preço'] * 1.05}
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()

novos_produtos = [
    {**produto, 'preço':produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')
print()





