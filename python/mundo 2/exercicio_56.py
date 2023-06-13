idadem = 0
idadef = 0
novaidade = 0

for x in range(1, 5):
    print(f'por favor, insira os dados da {x}° pessoa')
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    genero = input('''digite seu gênero, sendo:
    - (f) feminino
    - (m) masculino
    - (o) outros
    -> ''')

    novaidade = novaidade + idade

    if genero == 'm' and idade > idadem:
        idadem = idade
        nomem = nome
    if genero == 'f' and idade < 20:
        idadef = idadef + 1

media = novaidade/x
print(f'a média de idade do grupo é de {media} anos;')
print(f'o nome do homem mais velho é {nomem};')
print(f'e existe(m) {idadef} mulher(es) com menos de 20 anos.')
