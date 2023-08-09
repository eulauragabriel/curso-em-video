n = int(input('''insira um valor: 
-> '''))
r1 = input('''deseja continuar? (s/n)
-> ''')
maior = n
menor = n
soma = n
contador = 1
if r1 == "s":
    r = "s"
    while r == "s":
        n = int(input('''insira um valor: 
-> '''))
        r = input('''deseja continuar? (s/n)
-> ''')
        soma = soma + n
        contador = contador + 1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

media = soma/contador
if r1 != 's' or r != 'n':
            print('resposta inválida, o programa será encerrado!')
print(f"a média destes {contador} números é de {media}, sendo o maior número {maior} e o menor número {menor}.")