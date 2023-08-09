ncin = 0
nvin = 0
ndez = 0
num = 0
print('''-------------------------------------
          CAIXA ELETRÔNICO
-------------------------------------''')
v = int(input('insira o valor a ser sacado: '))
while v == 0:
    print('Valor inválido!')
    v = int(input('insira o valor a ser sacado: '))
    if v > 0:
        break
while v > 0:
    while v >= 50:
        ncin = ncin + 1
        v = v - 50
    print(f'Total de {ncin} notas de R$50,00')
    while v >= 20:
        nvin = nvin + 1
        v = v - 20
    print(f'Total de {nvin} notas de R$20,00')
    while v >= 10:
        ndez = ndez + 1
        v = v - 10
    print(f'Total de {ndez} notas de R$10,00')
    while v >= 1:
        num = num + 1
        v = v - 1
    print(f'Total de {num} notas de R$1,00')
print('-------------------------------------')
