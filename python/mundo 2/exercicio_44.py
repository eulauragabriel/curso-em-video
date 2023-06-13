v = float(input('insira o valor do produto: '))
c = int(input('''escolha uma condição de pagamento:
- à vista (1)
- à vista no cartão (2)
- em até 2x no cartão (3)
- em 3x ou mais no cartão (4) 
-> '''))
 
if c == 1:
    d = v * 10/100
    print(f'você terá um desconto de 10%, sendo assim o novo valor do produto será de R${v - d :.2f}!')
elif c == 2:
    d = v * 5/100
    print(f'você terá um desconto de 5%, sendo assim o novo valor do produto será de R${v - d :.2f}!')
elif c == 3:
    print(f'o valor final do produto será de R${v :.2f}!')
elif c == 4:
    j = v * 20/100
    print(f'você será cobrado 20% de juros, sendo assim o novo valor do produto será de R${v + j :.2f}!')
else:
    print('condição de pagamento inválida!')