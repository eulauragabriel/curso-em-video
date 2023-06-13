import random

jokenpo = ["pedra", "papel", "tesoura"]
pc = random.choice(jokenpo)

print("----- escolha entre pedra, papel e tesoura: -----")
vc = input("----> ")
print("------------ o computador escolheu: -------------")
print(f"----> {pc}")

if vc == "pedra":
    if pc == "tesoura":
        print("--------------- você ganhou!!! ------------------")
    elif pc == "papel":
        print("--------------- você perdeu!!! ------------------")
    elif pc == "pedra":
        print("------------- aconteceu um empate! --------------")
elif vc == "papel":
    if pc == "tesoura":
        print("--------------- você perdeu!!! ------------------")
    elif pc == "pedra":
        print("--------------- você ganhou!!! ------------------")
    elif pc == 'papel':
        print("------------- aconteceu um empate! --------------")
elif vc == "tesoura":
    if pc == "papel":
        print("--------------- você ganhou!!! ------------------")
    elif pc == "pedra":
        print("--------------- você perdeu!!! ------------------")
    elif pc == 'tesoura':
        print("------------- aconteceu um empate! --------------")
