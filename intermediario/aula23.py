"""
Introdução à list comprehension em python
list comprehension em python
list comprehensio é uma forma rápida para criar listas a 
partir de itaráveis
"""

#forma comum
print(list(range(10)))
print()

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

print()
#usando o list comprehension(pode fazer operações)
lista = [numero for numero in range(10)]
print(lista)

print()
lista = [ numero  * 2 for numero in range(10)]
print(lista)