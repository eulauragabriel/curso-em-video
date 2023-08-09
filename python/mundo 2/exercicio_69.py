r = "S"
m = 0
f = 0
i = 0
im = 0
while r == "S":
    print('''
---------------------------------
       CADASTRE UMA PESSOA
---------------------------------''')
    idade = int(input('Idade: '))
    if idade >= 18:
        i = i + 1
    sexo = input('Sexo: [M/F] ')
    if sexo == "M":
        m = m + 1
    elif sexo == "F":
        f = f + 1
    while sexo != "M" and sexo != "F":
        sexo = input('Sexo: [M/F] ')
    if idade <= 20 and sexo == "F":
        im = im + 1
    print("---------------------------------")
    r = input('Quer continuar? [S/N] ')
    while r != 'S' and r != 'N':
        r = input('Quer continuar? [S/N] ')
    if r == "N":
        break
print('''---------------------------------
       CADASTRO CONCLUÍDO
---------------------------------''')
print(f'''
[A] existem {i} pessoas com pelo menos 18 anos
[B] existem {m} homens cadastrados
[C] existem {im} mulheres com menos de 20 anos cadastradas''')
