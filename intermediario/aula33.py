"""
Introdução às Generator functions em python
generator = (n for n in range(1000000))
"""

#generator = (n for n in range(1000000))
#print(generator)


def generator(n=0):
    return 1

gen = generator(n=0)
print(gen)

print(40*'-')

def generator1(n=0):
    yield 1 #pause
    return 'ACABOU'
gen = generator1(n=0)
print(next(gen))
print(gen.__iter__())

print(40*'-')

def generator2(n=0):
    yield 1
    print('Continua...')
    yield 2 
    print('Mais uma vez...')
    yield 3
    print('Vou terminar')
    return 'Acabou'

gen = generator2(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))

print(40*'-')

def generator3(n=0):
    yield 1
    print('Continua...')
    yield 2 
    print('Mais uma vez...')
    yield 3
    print('Vou terminar')
    return 'Acabou'
#usando o for
gen = generator3(n=0)
for n in gen:
    print(n)

print(40*'-')

def generator4(n=0, maximun=10):
    while True:
        yield n
        n += 1
        if n >= maximun:
            return n

gen = generator4()
for n in gen:
    print(n)

print(40*'-')

gen = generator4(n=5, maximun=8)
for n in gen:
    print(n)

print(40*'-')

gen = generator4(maximun=1000000)
for n in gen:
    print(n)

print(40*'-')