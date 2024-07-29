"""
Generator expression, iterables e iterator(iteráveis e iteradores)
"""
iterable = ['Eu','Tenho','__iter__']
iterator = iterable.__iter__() #tem__iter__e__next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

#o iterator so chama o proximo valor, so isso.


