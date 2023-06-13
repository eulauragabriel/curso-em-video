import random

aluno1 = input("digite o nome do primeiro aluno: ")
aluno2 = input("digite o nome do segundo aluno: ")
aluno3 = input("digite o nome do terceiro aluno: ")
aluno4 = input("digite o nome do quarto aluno: ")

nomes = [aluno1, aluno2, aluno3, aluno4]
aluno = random.shuffle(nomes)

#print('a ordem de apresentação será: ')
#print(nomes)
#essa é a resolução do gustavo guanabara

print(f'a ordem dos alunos será:')
for aluno in nomes:
    print(aluno)
