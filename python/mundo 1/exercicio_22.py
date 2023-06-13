nome = input('digite seu nome completo: ')
mai = nome.upper() #todas as letras maiúsculas
min = nome.lower() #todas as letras minúsculas
letras = (len(nome.replace(" ",""))) #tira os espaços e conta quantas letras tem
lista = nome.split() #cria uma lista dos nomes
print(f'{mai} é o seu nome com todas as letras maiúsculas')
print(f'{min} é o seu nome com todas as letras minúsculas')
print(f'seu nome tem {letras} letras')
print (f'seu primeiro nome tem {len(lista[0])} letras')