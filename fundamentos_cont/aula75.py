#Desempacotando em chamadas de funções
#Desempacotamento em chamadas de metodos e funções

string = 'ABCD'
lista = ['Maria','Helena','Eduarda']
tupla = 'Python', 'é', 'legal'

a,b,c = lista
print(a,c)

for nome in lista:
    print(nome)
print(30*'-')

print(*lista)
print(*string)
print(*tupla)
print(30*'-')

salas = [ 
        ['M','H',],
        ['E',],
        ['L','J','E',],
        ]
print(salas)
print(30*'-')
print(*salas)
print(30*'-')
print(*salas, sep='\n')