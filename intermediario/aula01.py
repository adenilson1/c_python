"""
'Def' define uma função (def) personalizada.
Funções são trechos de código usados para replicar 
determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor esperdífico.
Por padrão funções python retornam nano (nada)
"""
#funcao sem parametro
def imprimir():
    print('várias')
    print('várias')
    print('várias')

imprimir()

def imprimir2 (a,b,c):
    print(a,b,c)

imprimir2(1,2,3)

def imprimir3(nome = 'Sem nome'):
    print(f'Olá, {nome}')

imprimir3('adenilson')
imprimir3()
