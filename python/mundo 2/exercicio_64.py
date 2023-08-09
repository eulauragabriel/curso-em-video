numero = 0
soma = 0
contador = 0
while numero != 999:
    numero = int(input('digite um número: '))
    soma = soma + numero 
    contador = contador + 1
print(f'foram digitador {contador - 1} números e {soma - 999} é a soma deles!')
