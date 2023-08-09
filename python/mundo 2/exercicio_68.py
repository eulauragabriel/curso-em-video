from random import randint

nr = 0
cont = 0
player = 0
jogo = 0
while player == jogo:
    nr = randint(1, 10)

    player = int(input('''
-----------------------------------
        JOGO ÍMPAR OU PAR
-----------------------------------
[1] para ímpar
[2] para par
-----------------------------------
--> '''))
    
    np = int(input('''
-----------------------------------
        JOGUE SEU NÚMERO
-----------------------------------
--> '''))
    
    nn = np + nr

    if nn % 2 == 0:
        jogo = 2
    elif nn % 2 != 0:
        jogo = 1
    
    print('''
-----------------------------------''')

    if player == jogo:
        print('VOCÊ GANHOU!')
        print(f'Você jogou {np} e o computador jogou {nr}, o valor era de {nr + np}!')
        print('-----------------------------------')
        cont = cont + 1
    else:
        print('VOCÊ PERDEU!')
        print(f'Você jogou {np} e o computador jogou {nr}, o valor era de {nr + np}!')
        print('-----------------------------------')
        break

print(f'Você teve {cont} vitória(s) consecutivas!')
print('-----------------------------------')