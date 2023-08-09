cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
n = int(input('insira um número de 0 a 20: '))

while n not in range(0, 21):
    n = int(input('Tente novamente. Insira um número de 0 a 20: '))

print(f'o número {n} por extenso é {cont[n]}')