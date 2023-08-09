a = 0
b = 1
c = 1
n = int(input('quantos elementos da sequência de fibonacci deseja vizualizar? '))
print(f'{a} -> ', end='')
while n > 1:
    print(f'{c} -> ', end='')
    c = b + a
    a = b
    b = c
    n = n - 1
print('the end!')