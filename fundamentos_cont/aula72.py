"""
split e join com list e str
split = divide uma string
join = une uma string
"""
frase = "Olha só que, coisa interessante"

lista_palavras = frase.split() # quebra em nos espaços da string
print(lista_palavras)

lista_frase = frase.split(',') # quebra onde tem a virgula
print(lista_frase)

#usando o for
for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip()) # strip - corta os espços no começo e no fim da string
    print(lista_frase[i].rstrip()) # rstrip - corta os espços da direita
    print(lista_frase[i].lstrip()) #corta os espaços da esquertda

lista_frase_1 = []
for i, frase in enumerate(lista_frase):
    lista_frase_1.append(lista_frase[i].strip())
print(lista_frase_1)


print(20*'-')

frases_unidas = '-'.join('abc')
print(frases_unidas)

frases_unidas = ','.join(lista_frase) # numeros nao iterados
print(frases_unidas)