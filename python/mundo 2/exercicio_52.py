d = 0
n = int(input("digite um número: "))
for x in range(1, n + 1):
    if n % x == 0:
        d = d + 1

if d == 2:
    print(f'''o número {n} é primo!
ele só é divisível por 1 e por ele mesmo!''')
    
if d > 2:
    print(f'''o número {n} não é primo!
ele é divisível por mais {d - 2} número(s) além de 1 e ele mesmo!''')