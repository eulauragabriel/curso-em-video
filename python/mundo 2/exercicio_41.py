from datetime import datetime

hoje = datetime.now().year

ano = int(input('digite o seu ano de nascimento: '))

idade = hoje - ano

print(f'você fez ou fará {idade} anos esse ano')
if idade <= 9:
    print('sua categoria é a mirim')
elif idade > 9 and idade <= 14:
    print('sua categoria é a infantil')
elif idade > 14 and idade <= 19:
    print('sua categoria é a junior')
elif idade > 19 and idade <= 20:
    print('sua categoria é a sênior')
else:
    print('sua categoria é a master')