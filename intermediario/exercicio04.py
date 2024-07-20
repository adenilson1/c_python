"""
Exercicio - Sistem de perguntas
"""

perguntas = [
    {
        'Pergunta':'Quanto é 2 + 2 ?',
        'Opções':['1','2','3','4'],
        'Resposta':'4'
    },
    {
        'Pergunta':'Quanto é 5 * 5 ?',
        'Opções':['25','55','10','50'],
        'Resposta':'25'
    },
    {
        'Pergunta':'Quanto é 10/2 ?',
        'Opções':['4','5','2','1'],
        'Resposta':'5'
    },
    {
        'Pergunta':'Quanto é 4 ** 3 ?',
        'Opções':['24','12','64','48'],
        'Resposta':'64'
    },

]

numero_acertos = 0
numero_erros = 0

for i in range(0,len(perguntas)):
        print('Pegunta:',perguntas[i].get('Pergunta'))
        print()
        print('Opções:')

        for j in range(0,len(perguntas[i]['Opções'])):
            print(f"{j}) {perguntas[i].get('Opções')[j]}")

            def resposta_certa(resposta):
                def resposta_digitada(n_numero):
                    if resposta == perguntas[i].get('Opções')[n_numero]:
                        return 'acertou'
                    else:
                        return 'errou'
                return resposta_digitada

        opcao = resposta_certa(perguntas[i].get('Resposta'))
        numero = input('Digite uma opção: ')

        try:
            n_numero = int(numero)
            perguntas[i].get('Opções','Inexiste')[n_numero]
        except:
 
             print('Digite uma opção válido')
             numero_erros +=1
             continue

        if opcao(n_numero) == 'acertou':
             numero_acertos +=1
             print(opcao(n_numero))
        else:
             numero_erros +=1
             print(opcao(n_numero))
        print()


print(f'Você teve {numero_acertos} acertos')
print(f'Você teve {numero_erros} erros')
            
            


  