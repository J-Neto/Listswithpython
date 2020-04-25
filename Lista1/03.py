#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
#calcule e imprima a média geral.

import random as r

#Define list length
listX = [0] * 15

#Generating random list
for i in range(len(listX)):
    rand_number = r.randint(0,10)
    listX[i] = rand_number

#Calculating mean
mean = (sum(listX))/len(listX)

#printing
print('As notas são: {} \nA média das notas é igual a {}'.format(listX, mean))