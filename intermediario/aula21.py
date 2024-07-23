"""
Funçẽos lambdas complexas
funcao lambda são funcões anonimas(sem nome),
nao tem parenteses e nao usa o return
"""

#Funções nomeadas

def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

"""
nota: nunca fazer isso -> funcao = lambda parametro:paramentro
"""

print(
    executa(
        lambda x,y: x+y, 2,3
    ),
    executa(soma,2,3)
)

print()
duplica = cria_multiplicador(2)
duplica = executa(
    lambda m:lambda n: n*m, 2
)

print(duplica(2),
      
      executa(
          lambda *args:sum(args), 1,2,3,4,5
      )
      )
