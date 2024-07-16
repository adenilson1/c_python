"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros
podem ter valores padrão. Caso o valor
não seja enviado pra o parâmetro, o valor 
padrão será usado.
Refatora: editar um código
nota: quando um parametro nao tem um argumento 
na execução da função o sistema dá problema
nota2: todo parametro que tem um valor 
padrão na definição da função, obriga que todos os 
outros padrões que vierem depois dele devem ter 
devem ter valores também
"""

def soma(x,y):
    print(x+y)
soma(1,2)
soma(3,5)
soma(100,200)

def soma2(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}',x+y+z)
    else:
        print(f'{x=} {y=}', x+y)
soma2(1,2)
soma2(3,5)
soma2(100,200)
soma2(7,9,0)
soma2(x=9, z=0, y=3)
