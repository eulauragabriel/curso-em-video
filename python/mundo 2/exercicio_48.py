soma = 0
for x in range(0, 501):
    if x % 2 != 0:
        if x % 3 == 0:
            soma = soma + x
print(f'a soma de todos os números ímpares e múltiplos de 3 no intervalo de 0 a 500 é {soma}')