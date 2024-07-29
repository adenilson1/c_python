"""
dir, hasattr e getattr em python
"""
string = 'Luiz'
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())
print()

string = 'Luiz'
metodo = 'lower'
if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string,metodo)())
else:
    print('Não existe metodo',metodo)