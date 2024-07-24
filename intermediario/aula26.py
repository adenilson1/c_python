"""
List comprehesion com mais um for
"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)
print()

lista = [
    (x,y) #map
    for x in range(3)
    for y in range(3)
]
print(lista)