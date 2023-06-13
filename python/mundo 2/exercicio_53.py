frase = input("digite uma frase: ")
frasao = frase.upper()
fraser = frasao.replace(" ", "")
tamanho = len(fraser)
inverso = ""

for letra in range(tamanho - 1, -1, -1):
    inverso = inverso + fraser[letra]

# começa pela última letra de fraser e vai adicionando ex:
# a = a + r
# ar = ar + u

print(f"{fraser} invertido fica {inverso}!")

if fraser == inverso:
    print("é um palíndromo!")
else:
    print("não é um palíndromo!")

# -1 -> ex: laura = range(0, 4) e len(5), para o programa não começar no 5 (pq é inverso), precisamos adicionar -1
# -1 -> o programa vai até a última letra que seria 0 mas ele para em um número antes então ele não leria o próprio 0
# -1 começar pelo final, inverso
