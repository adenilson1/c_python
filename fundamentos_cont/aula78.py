#calculando o primeiro digito

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
primeiro_digito = 0
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 +=(int(digito) * contador_regressivo_1)
    contador_regressivo_1 -=1
primeiro_digito = (resultado_1 * 10)%11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)