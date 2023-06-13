a = float(input('digite sua primeira nota: '))
b = float(input('digite sua segunda nota: '))
media = (a + b) / 2

print(f'média igual a {media :.1f}!')

if media >= 7.0:
    print('APROVADO')
elif media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')