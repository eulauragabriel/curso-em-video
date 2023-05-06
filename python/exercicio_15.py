km = float(input('digite a quantidade de km percorridos com seu carro alugado: '))
dias = int(input('digite a quantidade de dias que você utilizou seu carro alugado: '))
preco = 60*dias + 0.15*km
print(f'você deverá pagar R${preco :.2f}.')