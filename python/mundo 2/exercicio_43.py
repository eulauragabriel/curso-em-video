p = float(input('digite seu peso: '))
h = float(input('digite sua altura em m: '))
imc = p/(h**2)

print(f'seu imc é de {imc :.1f}')
if imc < 18.5:
    print('está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('está no peso ideal')
elif imc >= 25 and imc < 30:
    print('está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('está com obesidade')
else:
    print('está com obesidade mórbida')