import random

n1 = random.randint(0, 100)

n2 = int(input('tente adivinhar um número de 0 a 100: '))

if n2 == n1:
    print(f'acertou, o número correto é {n1}!')
else:
    print(f'você errou, o número era {n1}!')