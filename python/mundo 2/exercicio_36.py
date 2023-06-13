valor = float(input('digite o valor da casa: '))
salario = float(input('digite o seu salário: '))
anos = int(input('digite em quantos anos pretende pagar: '))

parcela = valor/(anos*12)
maxima = salario*30/100

if maxima >= parcela:
    print(f'você pode realizar um empréstimo para pagar R${parcela :.2f} por mês pois 30% do seu salário é R${maxima :.2f}!')
if maxima < parcela:
    print(f'você não pode realizar um empréstimo para pagar R${parcela :.2f} por mês pois 30% do seu salário é apenas {maxima :.2f}!')
