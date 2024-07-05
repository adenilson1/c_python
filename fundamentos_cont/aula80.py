#analise da validação do cpf
cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
primeiro_digito = 0
resultado_1 = 0
dez_digitos = cpf_enviado_usuario[:10]
segundo_digito = 0
contagem_regressiva_2 = 11
resultado_2 = 0

#primeiro digito
for digito in nove_digitos:
    resultado_1 +=(int(digito) * contador_regressivo_1)
    contador_regressivo_1 -=1
primeiro_digito = (resultado_1 * 10)%11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(f'primeiro digito é {primeiro_digito}')

#segundo digito
for digito_2 in dez_digitos:
    resultado_2 += (int(digito_2) * contagem_regressiva_2)
    contagem_regressiva_2 -=1
segundo_digito =(resultado_2 * 10)%11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f'segundo digito é {segundo_digito}') 

#validação
print(25*'-')
cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'CPF de nº {cpf_gerado_pelo_calculo} é válido')
else:
    print('CPF INVÁLIDO')