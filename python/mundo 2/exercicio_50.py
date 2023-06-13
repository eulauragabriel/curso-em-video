soma = 0
for x in range(0, 6):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        soma = soma + n 
print(f'a soma dos valores pares inseridos é de {soma}')