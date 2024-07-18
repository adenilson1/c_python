"""
Criar funçẽos que duplicam, triplicam e quadruplicam
o numero recebido como paramentro
"""

def multiplication_operation(multiplier_number):
    def number_operation(number):
        return number * multiplier_number
    return number_operation

doubles = multiplication_operation(2)
triples = multiplication_operation(3)
quadruples = multiplication_operation(4)


for number in [1,2,3,4,5]:
    print(number,doubles(number),triples(number),quadruples(number))