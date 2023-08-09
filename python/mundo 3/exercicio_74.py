from random import randint

a = randint(0, 50)
b = randint(0, 50)
c = randint(0, 50)
d = randint(0, 50)
e = randint(0, 50)

maior = a
menor = a

tupla = a, b, c, d, e
for letra in tupla:
    if letra > maior:
        maior = letra
    if letra < menor:
        menor = letra

print(f'na tupla aleatória {tupla} o maior número é {maior} e o menor número é {menor}')