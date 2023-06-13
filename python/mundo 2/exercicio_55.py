peso1 = float(input('digite o peso da 1° pessoa em kg: '))
menor = peso1
maior = peso1

for x in range(2, 6):
    peso = float(input(f'digite o peso da {x}° pessoa em kg: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'o menor peso foi {menor :.1f}kg e o maior peso foi {maior :.1f}kg')
