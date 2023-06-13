from math import factorial

n = int(input("digite um número: "))
print(f'a fatorial {n}! é: ')
f = factorial(n)
x = n
while x > 0:
    if x != 1:
        print(f"{x} x ", end="")
    else:
        print(f'{x} = ', end="")
    x = x - 1

print(f'{f}')
