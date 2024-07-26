#Dictionary comprehension e set comprehension
produtos = {
    'nome':'Caneta azul',
    'preço': 2.5,
    'categoria':'Escritório',

}

dc = {
    chave:valor 
    for chave, valor in produtos.items()

}
print(dc)
print()

dc = {
    chave:valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor in produtos.items()

}
print(dc)
print()

dc = {
    chave:valor 
    if isinstance(valor,(int,float)) else valor.upper()
    for chave, valor in produtos.items()
}
print(dc)
print()

dc = {
    chave:valor.upper()
    if isinstance(valor,str) else valor 
    for chave, valor in produtos.items()
    if chave == 'categoria'
}
print(dc)
print()


lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('b','valor a'),
]
dc = {
    chave:valor 
    for chave,valor in lista 
}
print(dc)
print()

#outra forma usando dict
print(dict(lista))
print()

#usando o set comprehension
s = {2**i for i in range(10)}
print(s)
print()

#usado outra forma set
print(set(range(10)))