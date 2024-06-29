"""
Operação ternário com python (if e else de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')
print(35*'-')
print('Valor' if False else 'Outro valor')
print(35*'-')
#colocando em uma variavel
digito = 9
condicao = 10 == 10
novo_digito = digito if condicao else 0
print(novo_digito)
print(35*'-')
valor = 10
novo_valor = valor if valor <=9 else 0
print(novo_valor)
print(35*'-')
#invertido
valor1 = 9
novo_valor1 = 0 if valor1 > 9 else valor1
print(novo_valor1)