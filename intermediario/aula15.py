"""
Introdução ao tipo set em puthon - conjuntos
sets- conjuntos em pythons (tipo set)
conjuntos são ensinados na matematica
representados graficamente pelo diagrama de Venn
sets em python são multáveis como valor interno

criando um set
set(iterável) ou (1,2,3)

sets são eficientes para remover valores duplicados de iterávies.
- eles não tem índexes
- eles não garantem ordem
- eles são iterávies (for,in, set in)

Métodos uteis
add, update, clear, discord
"""

s1 = set()
print(s1, type(s1))
print()

s2 = set('Luiz')
print(s2, type(s2))
print()
"""
nota: sets são parecidos com dicionarios de dados, mas sem a chave so
com o valor e não garante a ordem dos dados
"""

s1 = set() #set vazio
s2 = {'Luiz',1,2,3} # set com dados