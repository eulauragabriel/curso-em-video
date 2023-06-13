a = int(input("digite o valor da primeira reta: "))
b = int(input("digite o valor da segunda reta: "))
c = int(input("digite o valor da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("esses valores formam um triângulo equilátero")
    elif a == b or b == c or c == a:
        print("esses valores formam um triângulo isósceles")
    elif a != b != c:
        print("esse é um triângulo escaleno")
else:
    print("esses valores não formam um triângulo")
