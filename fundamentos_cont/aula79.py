"""
calculo do segundo digito
"""

cpf = '74682489070'
dez_digitos = cpf[:10]
segundo_digito = 0
contagem_regressiva_2 = 11
resultado_2 = 0

for digito_2 in dez_digitos:
    resultado_2 += (int(digito_2) * contagem_regressiva_2)
    contagem_regressiva_2 -=1
segundo_digito =(resultado_2 * 10)%11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(segundo_digito) 