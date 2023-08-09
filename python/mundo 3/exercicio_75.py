a = int(input('insira o 1° valor: '))
b = int(input('insira o 2° valor: '))
c = int(input('insira o 3° valor: '))
d = int(input('insira o 4° valor: '))

par = 0
tupla = a, b, c, d
for cont in tupla:
    if tupla.count(9) == True:
        cont = cont + 1
    while cont % 2 == 0:
        par = par, cont
        break
tres = tupla.index(3)
