print('----- digite três números diferentes -----')
a = int(input('digite seu primeiro número: '))
b = int(input('digite seu segundo número: '))
c = int(input('digite seu terceiro número: '))

if a > b and c:
    maior = a
if b > a and c:
    maior = b
if c > a and b:
    maior = c
if a < b and c:
    menor = a
if b < a and c:
    menor = b
if c < a and b:
    menor = c

print(f'{maior} é o maior e {menor} é o menor!')