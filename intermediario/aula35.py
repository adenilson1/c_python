#try, exception, else, finally

a = 18
b = 2

try:
    c = a / b
    print(b[0])
except ZeroDivisionError:
    print('Divisão por zero')
except NameError:
    print('Nome indefinido')
except TypeError:
    print('Variavel nao definida')