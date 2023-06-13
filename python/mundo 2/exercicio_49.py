num = int(input('digite um número: '))
print(f'a tabuada do {num} é:')
for x in range(1, 11):
    print(f'{num} x {x} = {x * num}')