from datetime import datetime

agora = datetime.now().year
ano = int(input('digite seu ano de nascimento: '))

idade = agora-ano
x = 18-idade
y = idade-18

if idade < 18:
    print(f'você ainda terá que se alistar ao serviço militar, daqui a {x} ano(s)!')
elif idade > 18:
    print(f'você já passou do tempo de alistamento militar, foi há {y} ano(s)!')
else:
    print('está na hora de se alistar para o serviço militar!')
