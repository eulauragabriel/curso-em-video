s = float(input('digite seu salário: '))

if s >= 1250.0:
    a = s*10/100
    p = 10
if s < 1250.0:
    a = s*15/100
    p = 15
aumento = s+a
print(f'seu salário de R${s :.2f} terá um aumento de {p}%, ou seja, R${a :.2f}')
print(f'seu novo salário será de R${aumento :.2f}')