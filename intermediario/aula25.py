"""
Filtro de dados em list comprehesion (filter)
sao colocados à direita 
"""

#importando pprint
import pprint
def p(v):
    pprint.pprint(v, sort_dicts = False, width=48)

lista = [
    n
    for n in range(10)
    if n > 5
    ]
p(lista)
print()

produtos = [
    {'nome':'p1', 'preço':10,},
    {'nome':'p2', 'preço':20,},
    {'nome':'p3', 'preço':30,},
]

novos_produtos = [
    {**produto, 'preço':produto['preço'] * 1.05} #map
    if produto ['preço'] > 20 else {**produto} 
    for produto in produtos
    if produto ['preço'] >=20 # filter
]
p(novos_produtos)


