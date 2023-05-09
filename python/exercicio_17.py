import math

co = int(input('digite o cateto oposto: '))
ca = int(input('digite o cateto adjacente: '))
h = co**2 + ca**2
print(f'a hipotenusa é {math.sqrt(h)}')
