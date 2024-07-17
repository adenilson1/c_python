"""
HIgher Order Function
Funções de primeira classe
"""

def saudacao(msg,name):
    return f'{msg}, {name} !'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao,'Bom dia','Adenilson')
)

print(
    executa(saudacao,'Boa noite','Maria')
)