#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
#calcule e imprima a média geral.


import random as r

listX = [0] * 10

for i in range(len(listX)):
    random_number = r.randint(0,100)
    listX[i] = random_number

max_number = max(listX)
min_number = min(listX)

print(listX)
print('o maior número é {}'.format(max_number))
print('o menor número é {}'.format(min_number))