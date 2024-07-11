"""
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados receber apenas o argumentos(valor)
"""

def soma(x,y):
    print(x+y)

soma(1,2)

def soma2(x,y):
    print(f'{x=} y={y}','|','x + y = ', x+y)

soma2(1,2)

def soma3(x,y,z):
    print(f'{x=} y={y} z={z}', '|','x+y+z = ', x+y+z)

soma3(1,2,3)
soma3(1,2,z=5)
soma3(1,y=2,z=4)