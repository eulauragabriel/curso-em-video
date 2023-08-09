c = "S"
total = 0
mil = 0
barato = 0
cont = 0
nome = 0
while c == "S" :
    print('''-------------------------------------
              PRODUTOS
-------------------------------------''')
    n = input('Nome: ')
    p = float(input('Preço: '))
    while cont == 0:
        barato = p
        nome = n
        cont = cont + 1
    total = total + p
    if p >= 1000:
        mil = mil + 1
    if p < barato:
        barato = p
        nome = n
    print('-------------------------------------')
    c = input('Deseja continuar? [S/N] ')
    while c != "S" and c != "N":
        c = input('Deseja continuar? [S/N] ')
    if c == "N":
        break
print(f'''-------------------------------------
[A] o total gasto na compra foi de R${total :.2f}
[B] {mil} produto(s) custa(m) mais de mil reais
[C] o produto mais barato é {nome}''')
 