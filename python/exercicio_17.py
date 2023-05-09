import math

co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
h = co**2 + ca**2
print(f'a hipotenusa é {math.sqrt(h) :.2f}')
