a = int(input("digite o valor da primeira reta: "))
b = int(input("digite o valor da segunda reta: "))
c = int(input("digite o valor da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("esses valores formam um triângulo!")
else:
    print("esses valores não formam um triângulo")
