"""
OPeradores importantes para o tipo set (conjunto)
"""

s1 = {1,2,3}
s2 = {2,3,4}

# | -> uniao
s3 = s1 | s2
print(s3)
print()

# & ->intersecção
s3 = s1 & s2
print(s3)
print()

# - -> diferença
s3 = s1 - s2
print(s3)
print()

s3 = s2 - s1
print(s3)
print()

# ^ -> simetrico: não importa a ordem
s3 = s1 ^ s2
print(s3)
print()