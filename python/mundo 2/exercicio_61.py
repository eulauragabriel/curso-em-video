a = int(input('insira o primeiro termo para uma PA: '))
r = int(input('insira a razão para essa PA: '))
p = 0
while p < 10:
    print(f'{a}', end=" -> ")
    a = a + r
    p = p + 1
print('FIM!')