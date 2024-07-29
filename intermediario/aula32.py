"""
Generator expression, iterable e iterator
"""
import sys

iterable = ['Eu', 'Tenho','__iter__']
iterator = iter(iterable) #tem__iter__e__next

#Generator é um iterator com função de pausar.

#generator = [n for n in range(100000)]
#print(generator)

generator = (n for n in range(100000))
print(generator)

lista = [n for n in range(100000)]
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)