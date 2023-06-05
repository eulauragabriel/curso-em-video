n = input('digite um número de 0 a 9999: ')
lista = n.strip()
u = lista[-1] if len(lista) >= 1 else 0
d = lista[-2] if len(lista) >= 2 else 0
c = lista[-3] if len(lista) >= 3 else 0
m = lista[-4] if len(lista) >= 4 else 0
print('seu número tem:')
print(f'unidade(s): {u}')
print(f'dezena(s): {d}')
print(f'centena(s): {c}')
print(f'milhar(es): {m}')

# boa parte do raciocínio foi meu mas me atrapalhei e pedi ajuda para AI
