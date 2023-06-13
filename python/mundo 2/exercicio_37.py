n = int(input('digite um número: '))
b = int(input('''para que base deseja converter esse número:
- para binário digite 1 
- para octal digite 2 
- para hexadecimal digite 3
- para todos acima digite 4
-> '''))

#esse [2:] serve para retirar o prefixo e deixar apenas o número

if b == 1:
    print(f'seu número em binário ficará {bin(n)[2:]}')
elif b == 2:
    print(f'seu número em octal ficará {oct(n)[2:]}')
elif b == 3:
    print(f'seu número em hexadecimal ficará {hex(n)[2:]}')
elif b == 4:
    print(f'seu número em binário ficará {bin(n)[2:]}, em octal ficará {oct(n)[2:]} e em hexadecimal ficará {hex(n)[2:]}')
else:
    print('número inválido')
