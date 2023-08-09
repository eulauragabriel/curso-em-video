from random import randint
r = randint(0, 10)
n = 11
t = 1
while r != n:
    n = int(input('tente adivinhar um valor de 0 a 10: '))
    if r != n:
        t = t + 1
        if r > n:
            print('um pouquinho mais...')
        elif r < n:
            print('um pouquinho menos...')
        print('tente novamente!')
if t != 1:
    print(f'você acertou depois de {t} tentativas!')
else:
    print('você acertou de primeira!')