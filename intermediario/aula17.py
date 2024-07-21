"""
Metpdos úteis do tipo set em python
"""

#add
s1 = set()
s1.add('Luiz')
s1.add(1)
print(s1)
print()
#update

s1.update(('Olá mundo',1,2,3,4))
print(s1)
print()

#discard
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
print()

#clear
s1.clear()
print(s1)
