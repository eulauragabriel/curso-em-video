n = 1
print('--------------------------------------')

while n > 0:
    n = int(input('''qual tabuada você quer ver? 
---> '''))
    print('--------------------------------------')
    if n < 0:
        break
    cont = 1
    while cont <= 10:
        tabuada = n * cont
        print(f'{n} x {cont} = {tabuada}')
        cont = cont + 1
    print('--------------------------------------')
print('o programa foi encerrado!')