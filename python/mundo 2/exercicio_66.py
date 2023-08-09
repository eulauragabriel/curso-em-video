n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('insira um número: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'foram digitados {cont} números e {soma} é a soma deles!')
