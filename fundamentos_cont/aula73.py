"""
LIsta de listas e sues indices
"""

salas = [
        # 0         1
        ['Maria', 'Helena', ], # 0
        # 0
        ['Elena',], # 1
        # 0        1        2
        ['Luiz','João','Eduarda',(0,10,20,30,40)] #2
]

print(salas)

print(30*'-')
#acesando o valor da lista
print(salas[1])
#acessando o valor da lista da lista
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(30*'-')
#buscando o valor 20
print(salas[2])
print(salas[2][3])
print(salas[2][3][2])
print(30*'-')
#usnado o for iteravel
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
