#try, except, else, finally

try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError as e:
    print('DIvisão por zero')
    print(e)
except NameError:
    print('Variavel indefinida')
except (TypeError, IndexError) as error:
    print('Tipo+Index')
    print('MSG: ',error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('Error desconhecido')
print('CONTINUA')