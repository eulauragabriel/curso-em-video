a = int(input('insira o primeiro termo para uma PA: '))
r = int(input('insira a razão para essa PA: '))
t = a
c = 1
termos = 0
mais = 10
while mais != 0:
    termos = termos + mais
    while c <= termos:
        print(f'{t}', end=" -> ")
        t = t + r
        c = c + 1
    print('PAUSA!')
    mais = int(input('quantos números a mais você deseja ver? '))
print('FIM!')