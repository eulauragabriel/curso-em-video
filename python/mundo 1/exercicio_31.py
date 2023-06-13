d = float(input("digite a distância da sua viagem em km: "))

if d <= 200:
    p = d * 0.5
    print(f"sua passagem de ônibus terá um custo de R${p :.2f}")
else:
    p = d * 0.45
    print(f"sua passagem de ônibus terá um custo de R${p :.2f}")
