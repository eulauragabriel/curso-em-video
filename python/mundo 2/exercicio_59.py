a = int(input('insira o primeiro valor: '))

maior = a
menor = a

b = int(input('insira o segundo valor: '))

if b > maior:
    maior = b
if b < menor:
    menor = b
m = 0
while m != 5:  
    m = int(input('''---------- menu: ---------- 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
-> '''))
    
    print('---------------------------')

    if m == 1:
        print(f'a soma de {a} + {b} = {a + b}')
    if m == 2:
        print(f'a multiplicação de {a} + {b} = {a * b}')
    if m == 3:
        print(f'o maior valor é {maior} e o menor valor é {menor}')
    if m == 4:
        a = int(input('insira um novo primeiro valor: '))
        b = int(input('insira um novo segundo valor: '))
        maior = a
        menor = a
        if b > maior:
            maior = b
        if b < menor:
            menor = b
    if m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        print('você inseriu um valor errado, tente novamente!')
    print('---------------------------')

print('você saiu do programa!')
print('---------------------------')
