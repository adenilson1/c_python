"""
Peculiaridades do tipo mutável set em python

operadores uteis:
*união | união (unio) - une
*intersecção & (insersection) - itens presentes em ambos
*diferença - itens presentes apenas no set da esquerda
*diferença simétrica - itens que não estão em embos

nota: set nao aceita list, dict e outro set dentro deles por
serem mutaveis
aceita apenas a tupla 
"""
s1 = {1,2,3,3,3,1} # elimina itens repetidos
print(s1)
print()
#passando lista para set

l1 =[1,2,3,3,3,3,4]
s1 = set(l1)
print(s1)
print()
#usando o for , in , not in para iterar um set
s1 = {1,2,3}
print(s1) # não tem indice, logo nao tem ordem
print()

print(3 in s1)
print(4 in s1)
for numero in s1:
    print(numero)