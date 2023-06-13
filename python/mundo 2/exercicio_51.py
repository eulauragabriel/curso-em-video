# an = a1 + (n-1)*r
a = int(input('digite um primeiro termo: '))
r = int(input('digite uma razão: '))
print('os 10 primeiros termos dessa progressão aritmética gerada são:')
for x in range(1, 11):
    p = a + (x - 1) * r
    print(f'{p}', end=' -> ')
print('FIM!')