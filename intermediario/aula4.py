"""
escopo de funções em python 
escopo significa o local onde aquele codigo pode atigir
existe o escopo global e local
o escopo global é o escopo onde todo o codigo é alcançavel
o escopo local é o escopo onde apenas nomes do mesmo local podem
ser alcançaveis
"""
x = 1
def escopo():
    x = 10
    def outra_funcao():
        x = 11 
        y = 2
        print(x,y)
    outra_funcao()
    print(x)
print(x)
escopo()
print(x)