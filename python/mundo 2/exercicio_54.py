from datetime import datetime 

atual = datetime.now().year
maior = 0
menor = 0

for x in range(0, 7):
    ano = int(input('digite seu ano de nascimento: '))
    if atual - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'{menor} pessoas são menores de idade e {maior} pessoas são maiores de idade!')
