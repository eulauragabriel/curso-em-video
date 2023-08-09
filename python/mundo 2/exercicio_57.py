sexo = 0
while sexo != "M" and sexo != "F":
    sexo = input('insira seu sexo (M/F): ').upper()
    if sexo != "M" and sexo != "F":
        print("o valor que você inseriu não é válido, tente novamente!")
print('cadastro de sexo concluído com sucesso!')