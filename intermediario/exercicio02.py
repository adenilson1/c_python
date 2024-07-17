#EXERCICIO COM FUNCOES

"""
1) CRIAR UMA FUNÇÃO QUE MULTIPLIQUE TODOS OS ARGUMENTOS
NÃO NOMEADOS RECEBIDOS.
RETORNE O TOTAL PARA UMA VARIAVEL E MOSTRE O VALOR DA 
VARIAVEL
"""

# funcao que multiplicar argumentos
def multiplicacao(*args):
    total = 1
    for number in args:
        total *= number
    return total 

#valor da variavel
resultado = multiplicacao(1,2,3,4,5,75,12)
print(resultado)

print(30*'-')
"""
2) CRIE UMA FUNCAÇÕ FALA SE O NUMERO É PAR OU IMPAR
RETORE SE O NUMERO É PAR OU IMPAR
"""
numero_str = input('Digite um numero :')

try:
        numero_float = float(numero_str)
except:
        print('Isso não é válido')

        
def par_impar(numero_float):
      
      if numero_float%2 == 0:
        return f'{numero_float} é Par'
      return f'{numero_float} é Ímpar'


numero_par_impar = par_impar(numero_float)
print(numero_par_impar)
           

















