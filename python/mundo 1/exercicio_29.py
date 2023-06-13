v = float(input('digite a velocidade do seu carro em km/h: '))
multa = (v-80)*7

if v > 80:
    print('você foi multado, está rápido demais!')
    print(f'pague uma multa de R${multa :.2f}!')
else:
    print('está dentro do limite, boa viagem!')