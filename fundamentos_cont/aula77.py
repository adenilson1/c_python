"""
Calculo do 1º digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF.
Multiplicando cada um dos valores po uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70(746824890)
10  9   8   7   6   5   4   3   2
7   4   6   8   2   4   8   9   0
70  36  48  56  12  20  32  27  0

Somar todos so resultados:
70+36+48+56+12+20+32+27+0=310
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão anterior por 11
3010 % 11 = 7
Se o resultado anterior por maior que 9
resultado é 0
Caso contrario:
resultado é o valor da conta
O primeiro digito do CPF é 7
"""